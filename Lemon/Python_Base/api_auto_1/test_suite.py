# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/15:14
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_suite.py
# @Software : PyCharm

import unittest
import HTMLTestRunnerNew
from Lemon.Python_Base.api_auto_1.test_http_request import TestHttpRequest
from Lemon.Python_Base.api_auto_1.do_excel import DoExcel
from Lemon.Python_Base.api_auto_1.read_config import ReadConfig

# 利用配置类，从配置文件case.conf读取出 session和option的值
button = ReadConfig().read_config('case.configs','CASE','button')
#
test_data = DoExcel().get_data('test_cases.xlsx','test_data',button)

suite = unittest.TestSuite()
for item in test_data:
    suite.addTest(TestHttpRequest(item['url'],
                                  eval(item['param']),
                                  item['http_method'],
                                  str(item['expected']),
                                  'test_api'))

with open('test_api.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)
