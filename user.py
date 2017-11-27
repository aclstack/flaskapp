# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from models import User

user = Blueprint('user', __name__)


@user.route('/<int:userid>')
def showUser(userid):
    try:
        u = User.query.filter_by(id=userid).first()
        return u.getUsername()
    except AttributeError:
        return "id为" + str(userid) + "的用户不存在"
