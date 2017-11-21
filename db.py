# -*- coding: utf-8 -*-

import MySQLdb
import hashlib
# 设置连接
conn = MySQLdb.connect('192.168.31.100', 'root', '123456', 'teacher')
# 创建游标
cur = conn.cursor()


def add_user(username, password):
    password = hashlib.md5(password).hexdigest()

    sql = "insert into user(name,passwd) values('%s', '%s')" % (username, password)
    try:
        cur.execute(sql)
        conn.commit()
        return 'OK'
    except MySQLdb.Error, MySQL_error:
        return MySQL_error.args[0]
    conn.close()


def check_user(username,password):
    password = hashlib.md5(password).hexdigest()
    sql = "select name from user where name='%s' and passwd='%s'" % (username, password)
    try:
        return cur.execute(sql)
    except MySQLdb.Error, MySQL_error:
        return 0
    conn.close()


