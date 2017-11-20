# -*- coding:utf-8 -*-
from wtforms import Form, TextField, PasswordField, validators


class User(object):
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


class LoginForm(Form):
    username = TextField("username", [validators.Required()])
    password = PasswordField("password", [validators.Required()])
