# -*- coding: utf-8 -*-
# @Time     : 2018/12/4/21:53
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson17_1130作业02_数据驱动延伸_v2.py
# @Software : PyCharm

"""1130作业的基础上做数据驱动的延伸"""
# 单元测试
'''
用例里面不能传参！

'''
import unittest
from Lemon.Python_Base.Lesson17_do_excel_20181203.Lesson17_1130作业01_数据驱动延伸 import HttpRequest

COOKIES=None
class TestHttpRequest(unittest.TestCase):  # 驼峰命名
    def setUp(self):    # self.url 放在setUP和初始化函数有没有区别？ -- 去复盘！！！
        self.url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'  # self/类/方法/属性--复盘！！！

    def tearDown(self):
        pass
    # 参数化第1种方法：初始化函数
    def __init__(self,param,http_method,methodname):  # 不能直接重写
        self.param = param
        self.http_method = http_method
        super(TestHttpRequest,self).__init__(methodname)  # 超继承--复盘！！！

    """ 
    父类：TestCase(初始化函数)--methodname
    子类：TestHttpRequest(初始化函数)--methodname
    """

    def test_login(self):  # 登陆成功
        res_login = HttpRequest().http_request(self.url,self.param,self.http_method) # 创建实例对象，调用对象方法
        print("登录请求的结果；",res_login.json())
        """以下是断言："""
        try:
            self.assertEqual('10001', res_login.json()['code'])  # 这里的self怎么用？复盘复盘复盘！！！
            # self.assertEqual('登录成功',res_login.json()['msg'])
        except AssertionError as e:
            print("断言错误的是：{}".format(e))
            raise e

        global COOKIES
        if res_login.cookies:  # 非空 非0, True
            COOKIES = res_login.cookies
    """只有当cookies不为空时，才去修改全局变量的值。即：登陆成功，修改COOKIES的值。登陆失败不修改。"""

    def test_error_pwd(self):  # 输入错误的密码
        res_login = HttpRequest().http_request(self.url, self.param, self.http_method)  # 创建实例对象，调用对象方法
        print("登录请求的结果；", res_login.json())
        """以下是断言："""
        try:
            self.assertEqual('20111', res_login.json()['code'])  # 这里的self怎么用？复盘复盘复盘！！！
            # self.assertEqual('用户名或密码错误',res_login.json()['msg'])
        except AssertionError as e:
            print("断言错误的是：{}".format(e))
            raise e

    def test_error_tel(self):  # 输入错误的手机号
        res_login = HttpRequest().http_request(self.url, self.param, self.http_method)  # 创建实例对象，调用对象方法
        print("登录请求的结果；", res_login.json())
        """以下是断言："""
        try:
            self.assertEqual('20111', res_login.json()['code'])  # 这里的self怎么用？复盘复盘复盘！！！
            # self.assertEqual('用户名或密码错误',res_login.json()['msg'])
        except AssertionError as e:
            print("断言错误的是：{}".format(e))
            raise e


'''
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
'''
