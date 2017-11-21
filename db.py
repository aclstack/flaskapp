# -*- coding: utf-8 -*-

import MySQLdb

# 设置连接
conn = MySQLdb.connect('192.168.31.100', 'root', '123456', 'teacher')
# 创建游标
cur = conn.cursor()
# 设置语句
db_name = raw_input()
sql = "select * from %s" % db_name
print sql
# 执行语句
cur.execute(sql)
# 输出结果
result = cur.fetchall()

for row in result:
    print row[0], row[1]

conn.close()

