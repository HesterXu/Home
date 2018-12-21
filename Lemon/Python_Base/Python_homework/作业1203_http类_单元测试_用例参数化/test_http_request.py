# -*- coding: utf-8 -*-
# @Time     : 2018/12/6/17:08
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : test_http_request.py
# @Software : PyCharm


import unittest
import pprint
from Lemon.Python_Base.Python_homework.作业1203_http类_单元测试_用例参数化.http_request import HttpRequest

class TestHttpRequest(unittest.TestCase):
    def __init__(self,url,param,http_method):
        pass
    super(__init__())p


    COOKIES = None
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_001_login(self,url,param,http_method):
        res = HttpRequest().http_request(url,param,http_method)
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

    # def test_002_recharge(self):
    #
    #     res_2 = HttpRequest().http_request(recharge, recharge_data, 'post',COOKIES)
    #     pprint.pprint(res_2.json())
    #     try:
    #         self.assertEqual('10001', res_2.json()['code'])
    #     except AssertionError as e:
    #         print("断言出错了：",e)
    #         raise e




