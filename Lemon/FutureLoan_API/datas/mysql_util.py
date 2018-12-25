# -*- coding: utf-8 -*-
# @Time     : 2018/12/24/7:25
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @Software : PyCharm
# @File     : mysql_util.py
# @Function : 

""""
1. 连接数据库
2. 编写一个sql
3. 建立游标
4. execute
"""
import pymysql
from Lemon.FutureLoan_API.common.config import CofigLoader

class MysqlUtil:

    def __init__(self):
        config = CofigLoader()
        host = config.get('mysql','host')
        port = config.getint('mysql','port')  # port是int类型
        user = config.get('mysql','user')
        password = config.get('mysql','password')
        # 建立连接，异常处理
        self.mysql = pymysql.connect(host=host, user=user, password=password,database=None,port=port)

    def fetch_one(self,sql):# 查询一条数据并返回
        cursor = self.mysql.cursor()  # 建立游标
        cursor.execute(sql)   # 根据sql执行查询
        return cursor.fetchone()


if __name__ == '__main__':
    sql = "select mobilephone from future.member where mobilephone != '' order by mobilephone desc limit 1;"
    mysql_util = MysqlUtil()
    results = mysql_util.fetch_one(sql)
    max_mobile = int(results[0]) + 1 # results: <class 'tuple'>  results[0]: <class 'str'>
    print(max_mobile)

