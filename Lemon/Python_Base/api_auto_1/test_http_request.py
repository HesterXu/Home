# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/15:14
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_http_request.py
# @Software : PyCharm


import unittest
from Lemon.Python_Base.api_auto_1.http_request import Http_Request

COOKIES = None

class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    def __init__(self,url,param,http_method,expected,methodName):
        self.url = url
        self.param = param
        self.http_method = http_method
        self.expected = expected
        super(TestHttpRequest,self).__init__(methodName)

    def test_api(self):
        global COOKIES
        res = Http_Request().http_request(self.url,self.param,self.http_method,COOKIES)
        print("请求结果是：",res.json())
        if res.cookies:
            COOKIES = res.cookies
        try:
            self.assertEqual(self.expected,res.json()['code'])
        except AssertionError as e:
            print("断言出错了: {}".format(e))
            raise e

