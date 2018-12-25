# -*- coding: utf-8 -*-
# @Time     : 2018/12/24/17:33
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @Software : PyCharm
# @File     : test.py
# @Function : 

'''1221作业
1.参数化excel登陆的测试数据，${register}
2.连接数据库，找到最大的手机号码并返回+1  # 从数据库找到的手机号放哪？
3.利用re模块来编写正则表达式查找变量${register}
4.把手机号替换上去  # 怎么取出来？
'''
import re
from Lemon.FutureLoan_API.datas.mysql_util import MysqlUtil


sql = "select mobilephone from future.member where mobilephone != '' order by mobilephone desc limit 1;"
mysql_util = MysqlUtil()
mobilephone_old = mysql_util.fetch_one(sql)[0]
print(mobilephone_old)


s = '{"mobilephone":"13537821056","pwd":"123456"}'  # 目标字符串
pattern = '\d{11}'
res = re.findall(pattern=pattern,string=s) # ['13537821056']
mobilephone = res[0]
print(mobilephone)  #  13537821056  <class 'str'>
s_new = s.replace(mobilephone, '13537821057')
print(s_new)
