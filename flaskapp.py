# -*- coding:utf-8 -*-
from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    #return 'Hello World!'
    return "反向路由" + url_for('query')


@app.route('/user', methods=['post'])
def usr():
    return 'This is post'


# http://127.0.0.1:5000/user/12345
@app.route('/user/<num>')
def user_id(num):
    return 'Hello' + num


# http://127.0.0.1:5000/query?id=12345
@app.route('/query')
def query():
    num = request.args.get('id')
    return 'you input id is: ' + num


@app.route('/ad')
def ad():
    return 'ok'

# 反向路由
@app.route('/route')
def route():
    #return "反向路由" + url_for('query')
    return '123456'



if __name__ == '__main__':
    app.run()
