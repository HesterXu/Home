# -*- coding: utf-8 -*-
# @Time     : 2018/12/5/7:30
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson17_1130作业03_数据驱动延伸_do_excel_v2.py
# @Software : PyCharm

# do_excel
import unittest
import HTMLTestRunnerNew
import openpyxl
from Lemon.Python_Base.Lesson17_do_excel_20181203.Lesson17_1130作业02_数据驱动延伸_v2 import TestHttpRequest

test_data = [{'param':{'mobilephone': 18688773467, 'pwd': '123456'},'http_method':'get','expected':'10001',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},

             {'param':{'mobilephone': 18688773467, 'pwd': '123456789'},'http_method':'post','expected':'20111',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},

             {'param':{'mobilephone': 13522332315, 'pwd': '123456'},'http_method':'get','expected':'20111',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},

             {'param':{'mobilephone': 18688773467, 'amount': '1000'},'http_method':'post','expected':'10001',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'}]

# 创建实例的方法
suite = unittest.TestSuite()
for item in test_data:   # for循环，复盘！！！
    suite.addTest(TestHttpRequest(item['url'],
                                  item['param'],
                                  item['http_method'],
                                  item['expected'],
                                  'test_api'))

# 将结果输出到txt文件中
# with open('UnittestTextReport_v2.txt','a') as f:
#     runner = unittest.TextTestRunner(stream = f,verbosity = 2)
#     runner.run(suite)

# 生成html报告
with open('test_report.html_v2','wb+') as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream = f,
                                           title='Http Request Report',
                                           description = 'Python12-Hester',
                                           verbosity = 2)
    runner.run(suite)

