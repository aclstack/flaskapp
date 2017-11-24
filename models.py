# -*- coding:utf-8 -*-
from wtforms import Form, TextField, PasswordField, validators
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import hashlib

# class User(object):
#     def __init__(self, user_id, username):
#         self.user_id = user_id
#         self.username = username


class LoginForm(Form):
    username = TextField("username", [validators.Required()])
    password = PasswordField("password", [validators.Required()])


# 实例化一个对象
app = Flask(__name__)
# 设置数据库信息
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@192.168.31.100/teacher"
# 忽略警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 生成db对象
db = SQLAlchemy(app)


# 继承了db的数据库模型，数据库模型提供了增删改查等一系列操作
class User(db.Model):

    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, username, password):

        self.username = username
        self.password = hashlib.md5(password).hexdigest()

    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception, e:
            db.session.rollback()
            if 'Duplicate entry' in e.args[0]:
                return 1062

# 初始化表结构
# db.create_all()

# print type(u.add())

