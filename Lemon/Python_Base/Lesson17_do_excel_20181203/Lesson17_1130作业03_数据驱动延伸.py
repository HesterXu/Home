# -*- coding: utf-8 -*-
# @Time     : 2018/12/4/22:26
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson17_1130作业03_数据驱动延伸.py
# @Software : PyCharm

import unittest
import HTMLTestRunner
# 第1，2种方法的导入： import测试类
# from Lemon.Python_Base.Lesson16_requests_20181130.homework_review_02 import TestHttpRequest
# 第3种方法的导入：    import模块
from Lemon.Python_Base.Lesson16_requests_20181130 import homework_review_02

login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
login_data = {'mobilephone': 18688773467, 'pwd': '123456789'}
login_data = {'mobilephone': 13522332315, 'pwd': '123456'}



# 第1种方法：创建addTest的实例，测试类的对象的形式来添加用例
# suite = unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_login'))
# suite.addTest(TestHttpRequest('test_recharge'))

# 第2种方法：loader 从测试类里面添加用例
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

# 第3种方法：loader 从模块里面添加用例
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(homework_review_02))

# 执行用例
# runner = unittest.TextTestRunner() # 创建对象runner，执行用例的执行者
# runner.run(suite)

# 将结果输出到txt文件中
# with open('UnittestTextReport_review.txt','a') as f:
#     runner = unittest.TextTestRunner(stream = f,verbosity = 2)
#     runner.run(suite)

# 生成html报告
# with open('test_report_review.html','wb+') as f:
#     runner = HTMLTestRunner.HTMLTestRunner(stream = f,
#                                            title='Http Request Report',
#                                            description = 'Python12-Hester',
#                                            verbosity = 2)
#     runner.run(suite)
