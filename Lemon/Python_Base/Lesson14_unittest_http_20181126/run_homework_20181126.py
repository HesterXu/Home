# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 11:13
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : run_homework_20181126.py
# @Software: PyCharm

import unittest
import HTMLTestRunner
# 方法二：
# from Lemon.Python_Base.Lesson14_unittest_http_20181126.unittest_homework_20181126 import mytest
# 方法三：
from Lemon.Python_Base.Lesson14_unittest_http_20181126 import unittest_homework_20181126

suite = unittest.TestSuite()  # 创建对象suite，存放用例

# 方法一：addTest()：专门来加用例的  测试类的对象的形式来添加用例
# suite.addTest(mytest('test_sum_01'))
# suite.addTest(mytest('test_sum_02'))
# suite.addTest(mytest('test_sub_01'))
# suite.addTest(mytest('test_sub_02'))
# suite.addTest(mytest('test_mul_01'))
# suite.addTest(mytest('test_mul_02'))
# suite.addTest(mytest('test_div_01'))
# suite.addTest(mytest('test_div_02'))
# suite.addTest(mytest('test_squ_01'))
# suite.addTest(mytest('test_squ_02'))

# 方法二：通过loader从指定的测试类里面添加用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(mytest)) # 对象suite调用方法addTest(),对象loader调用loadTestsFromTestCase()方法

# 方法三：通过loader从指定的模块里面添加用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(unittest_homework_20181126))

# 执行用例
# runner = unittest.TextTestRunner(verbosity=2)  # 创建对象runner，执行用例的执行者
# runner.run(suite)

# 将结果输出到txt文件中
# with open('UnittestTextReport.txt','a') as f:
#     runner = unittest.TextTestRunner(stream=f,verbosity=2)
#     runner.run(suite)

# 将结果输出到html文件中
with open('test_report.html','wb+') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                            title='MathTool Test Report',
                            description='Python12期 Hester',
                            verbosity=2)
    runner.run(suite)
