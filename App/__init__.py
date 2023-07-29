from flask import Flask
from .views import blue
from .exts import create_exts


def create_app():
    app = Flask(__name__)

    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qq134679@127.0.0.1/recruit'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    # 初始化插件
    create_exts(app=app)

    return app
