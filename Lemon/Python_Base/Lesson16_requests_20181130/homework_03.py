# -*- coding: utf-8 -*-
# @Time     : 2018/12/2/23:34
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : homework_03.py
# @Software : PyCharm

# 测试集，执行测试用例
import unittest
import HTMLTestRunner
# from Lemon.Python_Base.Lesson16_requests_20181130.homework_02 import mytest_login
# from Lemon.Python_Base.Lesson16_requests_20181130.homework_02 import mytest_recharge
from Lemon.Python_Base.Lesson16_requests_20181130 import homework_02

suite = unittest.TestSuite()  # 创建对象suite，存放用例

# 方法一：addTest()：专门来加用例的  测试类的对象的形式来添加用例
# suite.addTest(mytest_login('test_01_login_pass'))
# suite.addTest(mytest_login('test_02_login_fail'))
# suite.addTest(mytest_login('test_03_login_fail'))
# suite.addTest((mytest_recharge('test_01_recharge_pass')))
# suite.addTest((mytest_recharge('test_02_recharge_fail')))
# suite.addTest((mytest_recharge('test_03_recharge_fail')))
# suite.addTest((mytest_recharge('test_04_recharge_fail')))
# suite.addTest((mytest_recharge('test_05_recharge_fail')))

# 方法二：通过loader从指定的测试类里面添加用例
# 对象suite调用方法addTest(),对象loader调用loadTestsFromTestCase()方法
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(mytest_login))
# suite.addTest(loader.loadTestsFromTestCase(mytest_recharge))

# 方法三：通过loader从指定的模块里面添加用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(homework_02))

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
                            title='HTTP Request Test Report',
                            description='Python12 - Hester',
                            verbosity=2)
    runner.run(suite)
