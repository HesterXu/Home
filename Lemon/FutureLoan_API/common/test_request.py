# -*- coding: utf-8 -*-
# @Time     : 2018/12/21/16:27
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @Software : PyCharm
# @File     : test_request.py
# @Function : 

import unittest
import time
from Lemon.FutureLoan_API.common.request import Request
from ddt import ddt,data
from Lemon.FutureLoan_API.common.config import CofigLoader
from Lemon.FutureLoan_API.common.do_excel import DoExcel
#
# COOKIES = None
# # 利用我们写的配置类，从配置文件case.conf读取出 session和option的值
# button = CofigLoader().get('case.configs','CASE','button')
# # 调用do_excel模块里的DoExcel类里面的get_data方法， 方法需要几个参数：  文件名，表单名，配置值
# test_data = DoExcel().get_data('test_cases.xlsx','test_data',button)
#
# @ddt
# class TestRequest(unittest.TestCase):
#
#     @data(*test_data)
#     def test_api(self,item):
#         global COOKIES
#         print("目前正在执行第{}条用例：{}".format(item['case_id'],item['title']))
#         print("-----------------------开始检查URL地址--------------------------")
#         print('url:{}'.format(item['url']))
#
#         print("-----------------------开始检查param参数--------------------------")
#         print('param:{}'.format(item['param']))
#
#         print("-----------------------开始http请求--------------------------")
#         # res = Request().request(item['url'],eval(item['param']),item['http_method'],COOKIES)
#         # excel中的param是str，实际是字典
#         print("-----------------------结束http请求--------------------------")
#
#         print("请求结果是：",res.json())
#         if res.cookies:
#             COOKIES = res.cookies
#
#         print("-----------------------开始断言--------------------------")
#         try:
#             self.assertEqual(str(item['expected']),res.json()['code'])  # excel中的期望值是int，实际是str
#             # TestResult = 'PASS'
#         except AssertionError as e:
#             # my_logger.error("断言出错了: {}".format(e))
#             print("断言出错了: {}".format(e))
#             raise e
#             # TestResult = 'FAIL'
#         # print("本条用例的测试结论是：{}".format(TestResult))
#         # mylogger.info("本条用例的测试结论是：{}".format(TestResult))
#         print("-----------------------结束断言--------------------------")
#         time.sleep(1)
#

