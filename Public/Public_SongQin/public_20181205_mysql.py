# -*- coding: utf-8 -*-
# @Time     : 2018/12/5/15:08
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : public_20181205_mysql.py
# @Software : PyCharm

from pymysql import *
# 创建一个连接
conn = connect(host='127.0.0.1',port=3310,database='students',user='',password='',charset='utf8')
# 获取游标
cs1 = conn.cursors()
# 查询一条数据
count = csl.execute("select * from students")
result_1 = csl.fetchone()    # 返回的是元组

for i in range(count):
    result_2 = csl.fetchall()   # 返回的是元组
    print(result_1)
# 查询所有数据
result_2 = csl.fetchall()
# 打印数据
print(result_1)
print(result_2)
# 打印数据
commit()
# 修改数据
count = csl.execute('update students set  name="Hester" WHERE name="HesterXu"')
# 提交的操作
print(count)
conn.commit()


