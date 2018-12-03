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
# 测试用例
import unittest
from Lemon.Python_Base.Lesson16_requests_20181130.homework_01 import Myclass

"""测试登陆接口"""
class mytest_login(unittest.TestCase):
    login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
    login_data_2 = {'mobilephone': 18688773467, 'pwd': '111111'}
    login_data_3 = {'mobilephone': 0, 'pwd': '123456'}

    def setUp(self):     # 初始化工作
        print("do something before test.Prepare environment.")
    def tearDown(self):  # 退出清理工作
        print("do something after test.Clean up.")

    def test_01_login_pass(self):
        print("01：测试登录成功-------")
        actual = Myclass().http_request(self.login, self.login_data, 'get').json()['msg']
        expected = "登录成功"
        self.assertEqual(expected,actual)

    def test_02_login_fail(self):
        print("02：测试登陆失败：手机号正确，密码错误-------")
        actual = Myclass().http_request(self.login,self.login_data_2,'post').json()['msg']
        expected = "登录成功"
        self.assertNotEqual(expected,actual)

    def test_03_login_fail(self):
        print("03：测试登陆失败：手机号错误，密码正确-------")
        actual = Myclass().http_request(self.login, self.login_data_3, 'get').json()['msg']
        expected = "登录成功"
        self.assertNotEqual(expected, actual)

"""测试充值接口"""
class mytest_recharge(unittest.TestCase):
    login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
    login_data_2 = {'mobilephone': 18688773467, 'pwd': '000000'}
    res_login = Myclass().http_request(login, login_data, 'get')
    res_login_2 = Myclass().http_request(login, login_data_2, 'get')

    recharge = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
    recharge_data = {'mobilephone': 18688773467, 'amount': '1000'}
    recharge_data_2 = {'mobilephone': 18688773467, 'amount': '-100'}
    recharge_data_3 = {'mobilephone': 12222222222, 'amount': '1000'}

    def setUp(self):  # 初始化工作
        print("do something before test.Prepare environment.")
    def tearDown(self):  # 退出清理工作
        print("do something after test.Clean up.")
    def test_01_recharge_pass(self):
        print("01：测试充值成功-----------")
        res_recharge = Myclass().http_request(self.recharge,self.recharge_data,'post',
                                              cookies = self.res_login.cookies)
        actual = res_recharge.json()['msg']
        expected = '充值成功'
        self.assertEqual(expected,actual)

    def test_02_recharge_fail(self):
        print("02：测试充值失败：没有登陆-------")
        res_recharge = Myclass().http_request(self.recharge, self.recharge_data, 'post')
        actual = res_recharge.json()['msg']
        expected = '充值成功'
        self.assertNotEqual(expected, actual)

    def test_03_recharge_fail(self):
        print("03：测试充值失败：手机号正确，密码错误-------")
        res_recharge = Myclass().http_request(self.recharge, self.recharge_data, 'post',
                                              cookies = self.res_login_2.cookies)
        actual = res_recharge.json()['msg']
        expected = '充值成功'
        self.assertNotEqual(expected, actual)

    def test_04_recharge_fail(self):
        print("04：测试充值失败：登陆成功，充值金额为负数-------")
        res_recharge = Myclass().http_request(self.recharge, self.recharge_data_2, 'post',
                                              cookies=self.res_login.cookies)
        actual = res_recharge.json()['msg']
        expected = '充值成功'
        self.assertNotEqual(expected, actual)

    def test_05_recharge_fail(self):
        print("05：测试充值失败：登陆成功，充值手机号错误-------")
        res_recharge = Myclass().http_request(self.recharge, self.recharge_data_3, 'post',
                                              cookies=self.res_login.cookies)
        actual = res_recharge.json()['msg']
        expected = '充值成功'
        self.assertNotEqual(expected, actual)