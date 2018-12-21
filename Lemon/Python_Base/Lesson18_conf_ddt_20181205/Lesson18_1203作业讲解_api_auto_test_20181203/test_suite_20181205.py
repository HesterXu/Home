# -*- coding: utf-8 -*-
# @Time     : 2018/12/6/6:27
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_suite_20181205.py
# @Software : PyCharm

import unittest
import HTMLTestRunnerNew
from Lemon.Python_Base.Lesson18_conf_ddt_20181205.Lesson18_1203作业讲解_api_auto_test_20181203.\
    test_http_request_20181205 import TestHttpRequest
from Lemon.Python_Base.Lesson18_conf_ddt_20181205.Lesson18_1203作业讲解_api_auto_test_20181203.\
    do_excel_20181205 import DoExcel

test_data = DoExcel().get_data()

suite = unittest.TestSuite()
for item in test_data:
    suite.addTest(TestHttpRequest(item['url'],
                                  eval(item['param']),
                                  item['http_method'],
                                  str(item['expected']),
                                  'test_api'))  # 创建实例的方法

# 将结果输出到txt文件中
# with open('API_test_TextReport.txt','a') as f:
#     runner = unittest.TextTestRunner(stream = f,verbosity = 2)
#     runner.run(suite)

# 生成html报告
with open('test_api_report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)
