# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/15:14
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_suite.py
# @Software : PyCharm

import unittest
import HTMLTestRunnerNew
from Lemon.Python_Base.api_auto_3.test_http_request import TestHttpRequest
# from Lemon.Python_Base.api_auto_3.do_excel import DoExcel
# from Lemon.Python_Base.api_auto_3.read_config import ReadConfig

# 使用了ddt后不需要下面的代码了。
# # 利用我们写的配置类，从配置文件case.conf读取出 session和option的值
# button = ReadConfig().read_config('case.configs','CASE','button')
# 调用do_excel模块里的DoExcel类里面的get_data方法， 方法需要几个参数：  文件名，表单名，配置值
# test_data = DoExcel().get_data('test_cases.xlsx','test_data',button)

suite = unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_api')) # test_api方法被data装饰了，没有这个方法了。 创建对象时没有传参

# 使用ddt后就要用discover（web自动化），loader加载用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

# 使用了ddt后不需要下面的代码了。
# for item in test_data:
#     suite.addTest(TestHttpRequest(item['url'],
#                                   eval(item['param']),
#                                   item['http_method'],
#                                   str(item['expected']),
#                                   'test_api'))

with open('test_api.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)
