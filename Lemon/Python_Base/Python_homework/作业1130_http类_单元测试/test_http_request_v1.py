# -*- coding: utf-8 -*-
# @Time     : 2018/12/6/14:07
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_http_request_v1.py
# @Software : PyCharm

"""1130-写一个http请求的类 然后完成单元测试
1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
温馨提示：可以用到全部变量，global"""

import unittest
import pprint
from Lemon.Python_Base.Python_homework.作业1130_http类_单元测试.http_request_v1 import HttpRequest


class TestHttpRequest(unittest.TestCase):
    COOKIES = None
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_001_login(self):
        login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
        res = HttpRequest().http_request(login, login_data, 'get')
        print(res.json())
        try:
            self.assertEqual('10001',res.json()['code'])
        except AssertionError as e:
            print("断言出错了：",e)
            raise e
        global COOKIES
        if res.cookies:
            COOKIES = res.cookies
        """只有当cookies不为空时，才去修改全局变量的值。即：登陆成功，修改COOKIES的值。登陆失败不修改。"""

    def test_002_recharge(self):
        recharge = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
        recharge_data = {'mobilephone': 18688773467, 'amount': '1000'}
        res_2 = HttpRequest().http_request(recharge, recharge_data, 'post',COOKIES)
        pprint.pprint(res_2.json())
        try:
            self.assertEqual('10001', res_2.json()['code'])
        except AssertionError as e:
            print("断言出错了：",e)
            raise e









