# -*- coding: utf-8 -*-
# @Time     : 2018/12/2/23:34
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : homework_03.py
# @Software : PyCharm

# 测试集，执行测试用例
import unittest
import HTMLTestRunner
from Lemon.Python_Base.Lesson16_requests_20181130.homework_02 import mytest_login

suite = unittest.TestSuite()  # 创建对象suite，存放用例

suite.addTest(mytest_login('test_01_login'))

# 执行用例
runner = unittest.TextTestRunner(verbosity=2)  # 创建对象runner，执行用例的执行者
runner.run(suite)


'''
with open('test_report.html','wb+') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                            title='HTTP Request Test Report',
                            description='Python12 - Hester',
                            verbosity=2)
    runner.run(suite)
'''