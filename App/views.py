from flask import Blueprint, render_template, request
from .models import *

blue = Blueprint('user', __name__)


@blue.route('/index')  # 首页
def index():
    # 设置分页
    page = request.args.get('page', type=int, default=1)
    per_page = request.args.get('per_page', type=int, default=15)

    # 返回一个分页对象
    p = Webtab.query.paginate(page=page, per_page=per_page)

    return render_template('index.html', p=p)


@blue.route('/details/<int:id>')
def details(id):
    #用户点击后，获取到当时的ID，然后传入过来，去请求数据库找到对应的职位信息
    position_data = Webtab.query.get(id)
    return render_template('details.html', position_data=position_data)