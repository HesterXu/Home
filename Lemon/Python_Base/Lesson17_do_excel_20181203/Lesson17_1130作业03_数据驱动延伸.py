# -*- coding: utf-8 -*-
# @Time     : 2018/12/4/22:26
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson17_1130作业03_数据驱动延伸.py
# @Software : PyCharm

# 怎么做用例的参数化？？？
import unittest
import HTMLTestRunner
# 第1，2种方法的导入： import测试类
from Lemon.Python_Base.Lesson17_do_excel_20181203.Lesson17_1130作业02_数据驱动延伸_v2 import TestHttpRequest
# 第3种方法的导入：    import模块
# from Lemon.Python_Base.Lesson17_do_excel_20181203 import Lesson17_1130作业02_数据驱动延伸_v2

test_data = [{'param':{'mobilephone': 18688773467, 'pwd': '123456'},'http_method':'get','expected':'10001',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},

             {'param':{'mobilephone': 18688773467, 'pwd': '123456789'},'http_method':'post','expected':'20111',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},

             {'param':{'mobilephone': 13522332315, 'pwd': '123456'},'http_method':'get','expected':'20111',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},

             {'param':{'mobilephone': 18688773467, 'amount': '1000'},'http_method':'post','expected':'10001',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'}]

# 第1种方法：创建实例的方法
"""TestHttpRequest类继承了TestCase类，TestCase类有初始化函数，其中有个参数是methodname。
所以创建TestHttpRequest类的实例时，要传参methodname。多复盘，多练习，重点！！！
测试类TestHttpRequest中的测试方法test_login，是一条用例，用例里面不能传参！
把参数全部放在初始化函数里，创建实例的时候所有参数一起传"""
suite = unittest.TestSuite()
for item in test_data:   # for循环，复盘！！！
    suite.addTest(TestHttpRequest(item['url'],
                                  item['param'],
                                  item['http_method'],
                                  item['expected'],
                                  'test_api'))

# 将结果输出到txt文件中
with open('UnittestTextReport_v2.txt','a') as f:
    runner = unittest.TextTestRunner(stream = f,verbosity = 2)
    runner.run(suite)















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



#
# # 生成html报告
# with open('test_report.html','wb+') as f:
#     runner = HTMLTestRunner.HTMLTestRunner(stream = f,
#                                            title='Http Request Report',
#                                            description = 'Python12-Hester',
#                                            verbosity = 2)
#     runner.run(suite)
#

