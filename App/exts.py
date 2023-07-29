#插件管理
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_exts(app):
    db.init_app(app=app)

