# -*- coding: utf-8 -*-
# @Time     : 2018/12/6/17:08
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_suite.py
# @Software : PyCharm


import unittest
import HTMLTestRunnerNew
from Lemon.Python_Base.Python_homework.作业1203_http类_单元测试_用例参数化.test_http_request import TestHttpRequest


login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
recharge = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
recharge_data = {'mobilephone': 18688773467, 'amount': '1000'}

suite = unittest.TestSuite()
suite.addTest(TestHttpRequest('test_001_login'))



with open('test_report_v1.html','wb+') as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream = f,
                                           title='Http Request Report',
                                           description = 'Python12',
                                           tester='Hester Xu',
                                           verbosity = 2)
    runner.run(suite)
