from .exts import *


class Webtab(db.Model):
    __tablename__ = 'webtab'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    money = db.Column(db.String(50))
    city = db.Column(db.String(50))
    time = db.Column(db.String(50))
    companyname = db.Column(db.String(100))
    level = db.Column(db.String(50))
    skill = db.Column(db.Text)
    degree = db.Column(db.String(50))
    url = db.Column(db.Text)
    site = db.Column(db.String(300))
    detail = db.Column(db.Text)

