# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/15:14
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_suite.py
# @Software : PyCharm

import unittest
import HTMLTestRunnerNew
from Lemon.Python_Base.api_auto_4.common.test_http_request import TestHttpRequest
from Lemon.Python_Base.api_auto_4.common import project_path

suite = unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_api'))    # test_api方法被data装饰了，没有这个方法了。 创建对象时没有传参

# 使用ddt后就要用discover（web自动化），loader加载用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(project_path.report_path,'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)

