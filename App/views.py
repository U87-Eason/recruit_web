from flask import Blueprint, render_template, request, url_for, flash, redirect
from .models import *

blue = Blueprint('user', __name__)


@blue.route('/')  # 首页
def index_view():
    user_cookie = request.cookies.get('user_id')  # 用get是因为，当时设置cookie时候用用户ID去设置了cookie
    if user_cookie:  # 如果用户存在，我们就去找这个用户
        user = Userdata.query.get(user_cookie)

        # 设置分页
        page = request.args.get('page', type=int, default=1)
        per_page = request.args.get('per_page', type=int, default=15)

        # 返回一个分页对象
        p = Webtab.query.paginate(page=page, per_page=per_page)

        return render_template('index.html', p=p, user=user)
    return redirect(url_for('user.login_view'))


@blue.route('/register', methods=['GET', 'POST'])  # 注册页面视图函数
def register_view():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        if not nickname or not password or not confirmPassword:
            flash('所以字段都是必须要填写完整')
        elif Userdata.query.filter_by(name=nickname).first():
            flash('你注册账号已经存在，请换一下用户名')
        elif password != confirmPassword:
            flash('您的两次密码不一致')
        else:
            userdata = Userdata()
            userdata.name = nickname
            userdata.password = password

            db.session.add(userdata)
            db.session.commit()

            return redirect(url_for('user.login_view'))

        return render_template('register.html')

    return render_template('register.html')


@blue.route('/login', methods=['GET', 'POST'])  # 登录页面视图函数
def login_view():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        password = request.form.get('password')

        if not mobile or not password:
            flash('所有字段都是必须要填写完整')
        else:
            userdata = Userdata.query.filter_by(name=mobile, password=password).first()
            if userdata:
                # 登录成功
                response = redirect(url_for('user.index_view'))
                response.set_cookie('user_id', str(userdata.id), max_age=7 * 24 * 3600)
                return response
            else:
                flash('你的账户或者密码错误')
                return redirect(url_for('user.login_view'))

    return render_template('login.html')


@blue.route('/delete/user')  # 退出登录
def delete_user():
    response = redirect(url_for('user.index_view'))

    response.delete_cookie('user_id')
    return response


@blue.route('/details/<int:id>')  # 详情页内容视图函数
def details(id):
    user_cookie = request.cookies.get('user_id')  # 用get是因为，当时设置cookie时候用用户ID去设置了cookie
    if user_cookie:  # 如果用户存在，我们就去找这个用户
        user = Userdata.query.get(user_cookie)
        # 用户点击后，获取到当时的ID，然后传入过来，去请求数据库找到对应的职位信息
        position_data = Webtab.query.get(id)
        return render_template('details.html', position_data=position_data, user=user)

    return redirect(url_for('user.login_view'))


