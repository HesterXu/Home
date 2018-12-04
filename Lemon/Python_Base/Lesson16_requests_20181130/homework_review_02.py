# -*- coding: utf-8 -*-
# @Time     : 2018/12/4/10:32
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : homework_review_02.py
# @Software : PyCharm

# 单元测试
import unittest
from Lemon.Python_Base.Lesson16_requests_20181130.homework_review_01 import HttpRequest

COOKIES=None
class TestHttpRequest(unittest.TestCase):  # 驼峰命名
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_login(self): #登陆
        login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
        res_login = HttpRequest().http_request(login,login_data,'get') # 创建实例对象，调用对象方法
        print("登录请求的结果；",res_login.json())
        """以下是断言："""
        try:
            self.assertEqual('10001',res_login.json()['code'])   # 这里的self怎么用？复盘复盘复盘！！！
            # self.assertEqual('登录成功',res_login.json()['msg'])
        except AssertionError as e:
            print("断言错误的是：{}".format(e))
            raise e

        global COOKIES
        if res_login.cookies:  # 非空 非0, True
            COOKIES = res_login.cookies
            """只有当cookies不为空时，才去修改全局变量的值。即：登陆成功，修改COOKIES的值。登陆失败不修改。"""

    def test_recharge(self): #充值
        recharge = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
        recharge_data = {'mobilephone': 18688773467, 'amount': '1000'}
        res_recharge = HttpRequest().http_request(recharge,recharge_data,'post',COOKIES) #怎么拿到cookies?全局变量COOKIES
        print("充值请求的结果；",res_recharge.json())
        """以下是断言："""
        try:
            self.assertEqual('10001',res_recharge.json()['code'])
            # self.assertEqual('充值成功',res_recharge.json()['msg'])
        except AssertionError as e:
            print("断言错误的是：{}".format(e))
            raise e
