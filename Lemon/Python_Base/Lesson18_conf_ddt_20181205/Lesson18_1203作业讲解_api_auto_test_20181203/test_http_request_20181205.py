# -*- coding: utf-8 -*-
# @Time     : 2018/12/6/6:26
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_http_request_20181205.py
# @Software : PyCharm

import unittest
from Lemon.Python_Base.Lesson18_conf_ddt_20181205.Lesson18_1203作业讲解_api_auto_test_20181203.\
    http_request_20181205 import Http_Request

COOKIES = None
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    # def tearDown(self):
    #     pass

    def __init__(self,url,param,http_method,expected,methodName):  # 不能直接重写，父类TestCase的初始化函数有参数
        self.url = url
        self.param = param    # 初始化函数中的属性其他函数中都可以用
        self.http_method = http_method
        self.expected = expected
        super(TestHttpRequest,self).__init__(methodName)  # 超继承，先是子类，根据子类找到父类，调用父类里面的的方法，--复盘！！！

    def test_api(self):
        global COOKIES
        res = Http_Request().http_request(self.url,self.param,self.http_method,COOKIES) # 创建实例对象，调用对象方法
        print("请求的结果；",res.json())
        if res.cookies:  # True
            COOKIES = res.cookies
        """以下是断言："""
        try:
            self.assertEqual(str(self.expected), res.json()['code'])  # 这里的self怎么用？复盘复盘复盘！！！
        except AssertionError as e:
            print("断言错误的是：{}".format(e))
            raise e

if __name__ == '__main__':
    unittest.main()
