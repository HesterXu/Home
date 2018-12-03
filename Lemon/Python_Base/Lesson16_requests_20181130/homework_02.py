# -*- coding: utf-8 -*-
# @Time     : 2018/12/2/23:31
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : homework_02.py
# @Software : PyCharm
'''
写一个http请求的类 然后完成单元测试
1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
'''
'''
单元测试：
1.登陆：登陆地址  手机号  密码 
（1）- 登陆成功
（2）- 手机号正确，密码错误
（3）- 手机号错误，密码正确
（4）- 登陆地址错误
（5）- 手机号，密码都错误
（6）- 手机号为空或不存在
（7）- 密码为空

2.充值：充值地址  手机号  充值金额  登陆（登陆地址  手机号  密码）
（1）- 充值成功
（2）- 没有登陆
（3）- 充值金额为负
（4）- 充值地址错误
（5）- 手机号不存在
'''
# 测试用例
import unittest
from Lemon.Python_Base.Lesson16_requests_20181130.homework_01 import Myclass

"""Test res_login = r.http_request(login, login_data, 'get')"""
class mytest_login(unittest.TestCase):
    login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    login_data = {'mobilephone': 18688773467, 'pwd': '123456'}

    def setUp(self):     # 初始化工作
        print("do something before test.Prepare environment.")
    def tearDown(self):  # 退出清理工作
        print("do something after test.Clean up.")
    def test_01_login(self):
        global login
        global login_data
        print("01：测试登录成功-------")
        actual = Myclass().http_request(self.login, self.login_data, 'get')
        expected = "登录成功"
        self.assertEqual(expected,actual)

    def test_login_02(self):
        pass

class mytest_recharge(unittest.TestCase):
    def test_recharge_01(self):
        pass

