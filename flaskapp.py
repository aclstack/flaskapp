# -*- coding:utf-8 -*-
from flask import Flask, request, url_for, render_template
from models import User
app = Flask(__name__)


@app.route('/')
def hello_world():
    world = "Hello World"
    return render_template('index.html', world=world)


@app.route('/user')
def usr_index():
    user = User(1, "test")
    return render_template('user_index.html', user=user)


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
    return "反向路由" + url_for('query')


if __name__ == '__main__':
    app.run()

#测试