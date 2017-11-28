# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from userAPI import *
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
api = Api(app)

api.add_resource(Authentication, '/auth')

if __name__ == '__main__':
    app.run(port=9999)
