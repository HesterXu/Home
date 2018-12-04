# -*- coding: utf-8 -*-
# @Time     : 2018/12/4/21:53
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson17_1130作业02_数据驱动延伸_v2.py
# @Software : PyCharm

# 单元测试

import unittest
from Lemon.Python_Base.Lesson17_do_excel_20181203.Lesson17_1130作业01_数据驱动延伸 import HttpRequest

COOKIES=None
class TestHttpRequest(unittest.TestCase):  # 驼峰命名 测试类的类名
    """
    self.url 放在setUp和初始化函数中有没有区别??? 创建TestHttpRequest类的实例时，因为self.url在setUp里面，所以不传参，-- 去复盘！！！
    def setUp(self):
        self.url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'  # self/类/方法/属性--复盘！！！
    """
    def setUp(self):
        pass
    def tearDown(self):
        pass
    # 参数化第1种方法：初始化函数
    def __init__(self,url,param,http_method,expected,methodName):  # 不能直接重写，父类TestCase的初始化函数有参数
        self.url = url
        self.param = param    # 初始化函数中的属性其他函数中都可以用
        self.http_method = http_method
        self.expected = expected
        super(TestHttpRequest,self).__init__(methodName)  # 超继承，先是子类，根据子类找到父类，调用父类里面的的方法，--复盘！！！
    '''
    def test_login(self):  # 登陆成功
        res_login = HttpRequest().http_request(self.url,self.param,self.http_method) # 创建实例对象，调用对象方法
        print("登录请求的结果；",res_login.json())
    '''
    def test_api(self):
        res = HttpRequest().http_request(self.url,self.param,self.http_method,COOKIES) # 创建实例对象，调用对象方法
        print("请求的结果；",res.json())
        global COOKIES
        if res.cookies:  # True
            COOKIES = res.cookies
        """只有当cookies不为空时，才去修改全局变量的值。即：登陆成功，修改COOKIES的值。登陆失败不修改。"""

        """以下是断言："""
        try:
            self.assertEqual(self.expected, res.json()['code'])  # 这里的self怎么用？复盘复盘复盘！！！
            # self.assertEqual('登录成功',res_login.json()['msg'])
        except AssertionError as e:
            print("断言错误的是：{}".format(e))
            raise e

'''
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


if __name__ == '__main__':
    unittest.main()
