# -*- coding: utf-8 -*-
# @Time     : 2018/12/22/6:18
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @Software : PyCharm
# @File     : test_login.py
# @Function : 

'''1221作业
1.参数化excel登陆的测试数据，${register}
2.连接数据库，找到最大的手机号码并返回+1  # 从数据库找到的手机号放哪？
3.利用re模块来编写正则表达式查找变量${register}
4.把手机号替换上去  # 怎么取出来？
'''

import unittest
import json
from Lemon.FutureLoan_API.common.do_excel import DoExcel
from Lemon.FutureLoan_API.common import contants
from Lemon.FutureLoan_API.common.request import Request
from ddt import ddt,data,unpack

do_excel = DoExcel(file_name=contants.case_file)  # 实例化一个DoExcel对象
cases = do_excel.get_cases('login')  # 返回一个case列表，由一个个Case对象/实例组成

@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        print("测试准备")

    # def test_login(self):
    #     do_excel = DoExcel(file_name=contants.case_file)  # 实例化一个DoExcel对象
    #     cases = do_excel.get_cases('login')  # 返回一个case列表，由一个个Case对象/实例组成
    #     for case in cases:
    #         data = json.loads(case.data)   # 从excel中取到的data是一个字符串，把字符串转为字典
    #         resp = Request(method=case.method,url=case.url,data=data)
    #         print("status_code：", resp.get_status_code())  # 打印响应码
    #         resp_dict = resp.get_json()  # 获取请求响应，字典
    #         print("resp_dict ：", resp_dict)
    #         self.assertEqual(case.expected,resp.get_text())  # text???json????

    """拓展：file_data测试方法装饰器，读取文件数据（json/yaml），parameterized模块"""
    @data(*cases)  # 传进来cases列表
    def test_login(self,case):  # 用case变量接收传进来的数据
        data = json.loads(case.data)   # 从excel中取到的data是一个字符串，把字符串转为字典
        # 在这里写一个正则表达式，查找到手机号并替换掉
        # s = find_mobi(data)

        resp = Request(method=case.method,url=case.url,data=data)
        print("status_code：", resp.get_status_code())  # 打印响应码
        resp_dict = resp.get_json()  # 获取请求响应，字典
        self.assertEqual(case.expected,resp.get_text())  # text???json????

    def test_reqister(self):
        pass

    def tearDown(self):
        print("测试清除")
