# -*- coding: utf-8 -*-
# @Time     : 2018/12/6/14:14
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_suite_v1.py
# @Software : PyCharm

"""1130-写一个http请求的类 然后完成单元测试
1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
温馨提示：可以用到全部变量，global"""
import unittest
import HTMLTestRunnerNew
from Lemon.Python_Base.Python_homework.作业1130_http类_单元测试.test_http_request_v1 import TestHttpRequest

suite = unittest.TestSuite()
suite.addTest(TestHttpRequest('test_001_login'))
suite.addTest(TestHttpRequest('test_002_recharge'))


# with open('Http RequestTextReport_v1.txt','a') as f:
#     runner = unittest.TextTestRunner(stream = f,verbosity = 2)
#     runner.run(suite)


# runner = unittest.TextTestRunner()
# runner.run(suite)
#
with open('test_report_v1.html','wb+') as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream = f,
                                           title='Http Request Report',
                                           description = 'Python12',
                                           tester='Hester Xu',
                                           verbosity = 2)
    runner.run(suite)

