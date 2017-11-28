# -*- coding: utf-8 -*-

from flask_restful import reqparse, Resource
from models import User
from JsonObject import JsonObject
import sys

reload(sys)
sys.setdefaultencoding('utf8')
auth = reqparse.RequestParser()


class Authentication(Resource):
    def get(self):
        pass

    def post(self):
        auth.add_argument("username", required=True, help="用户名是必传内容")
        auth.add_argument("password", required=True, help="密码是必传内容")
        args = auth.parse_args()
        username = args['username']
        password = args['password']
        u = User(username, password)
        jsobj = JsonObject()
        if u.check_user():
            jsobj.put("code", "1")
            jsobj.put("desc", "用户存在")
        else:
            jsobj.put("code", "2")
            jsobj.put("desc", "用户不存在")
        print jsobj.getJson()
        return jsobj.getJson(), 200
