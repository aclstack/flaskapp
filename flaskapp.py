# -*- coding:utf-8 -*-
from flask import Flask, request, url_for, render_template, flash, abort, redirect
from models import User, LoginForm

# 让flash支持中文输出
import sys
reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.secret_key = '1234'


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/user')
def usr_index():
    user = User(1, "test")
    return render_template('user_index.html', user=user)

#http://127.0.0.1:5000/query?id=12345
# @app.route('/query_user')
# def query_user():
#     name = request.args.get('id')
#     return render_template('user_index.html', id=name)


# http://127.0.0.1:5000/user/12345
@app.route('/user/<user_id>')
def user_id(user_id):
    if int(user_id) == 1:
        flash('欢迎你 张三同学')
        return render_template('user.html')
    else:
        abort(404)


@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, 'Mike')
    return render_template('user_id.html', user=user)


@app.route('/users')
def user_list():
    users = []
    for i in range(1,11):
        user = User(i, 'Mike' + str(i))
        users.append(user)
    return render_template('user_list.html', users=users)


@app.route('/one')
def one():
    return render_template('one_base.html')


@app.route('/two')
def two():
    return render_template('two_base.html')


@app.route('/login', methods=['GET', 'post'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username:
            flash('请输入用户名', 'user_error')
            return render_template('login.html', username=username, password=password)
        if not password:
            flash('请输入密码', 'password_error')
            return render_template('login.html', username=username, password=password)
        if username == 'admin' and password == '123456':
            return redirect('https://www.baidu.com')
        else:
            message = 'Login Failed'
            return render_template('login.html', message=message)
    return render_template('login.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    MyForm = LoginForm(request.form)
    if request.method == 'POST':
        username = MyForm.username.data
        password = MyForm.password.data
        if username == 'admin' and password == '123456':
            return redirect('https://www.baidu.com')
        else:
            message = 'Login Failed'
            return render_template('new.html', form=MyForm, message=message)
    return render_template('new.html', form=MyForm)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def not_found(e):
    return render_template('500.html')


# 反向路由
@app.route('/route')
def route():
    return "反向路由" + url_for('query')


if __name__ == '__main__':
    app.run()

