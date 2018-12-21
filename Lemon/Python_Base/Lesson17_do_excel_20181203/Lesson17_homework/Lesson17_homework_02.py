# -*- coding: utf-8 -*-
# @Time     : 2018/12/5/11:02
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson17_homework_02.py
# @Software : PyCharm

"""1203-在1130作业的基础上完成测试用例的参数化
1：根据老师上课讲解的测试用例参数化，去写单元测试用例以及用到超继承
2：把所有的测试用例数据存到Excel中，然后写一个类do_excel，完成测试数据的读取
3：利用do_excel类读取到的测试数据 传给1203课堂上讲解的test_suite，完成测试用例的加载。
4：要求：登录3条用例 充值3条用例
5：请给用例加上断言 以及异常处理，断言可以用code 也可以用msg或者是用整段信息都OK，最后要有测试报告出具
"""
# 写单元测试用例
import unittest
from Lemon.Python_Base.Lesson17_do_excel_20181203.Lesson17_homework.Lesson17_homework_01 import HttpRequest

COOKIES = None
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def __init__(self,url,param,http_method,expected,methodName):  # 不能直接重写，父类TestCase的初始化函数有参数
        self.url = url
        self.param = param    # 初始化函数中的属性其他函数中都可以用
        self.http_method = http_method
        self.expected = expected
        super(TestHttpRequest,self).__init__(methodName)  # 超继承，先是子类，根据子类找到父类，调用父类里面的的方法，--复盘！！！

    def test_api(self):
        global COOKIES
        res = HttpRequest().http_request(self.url,self.param,self.http_method,COOKIES) # 创建实例对象，调用对象方法
        print("请求的结果；",res.json())
        if res.cookies:  # True
            COOKIES = res.cookies
        """以下是断言："""
        try:
            self.assertEqual(self.expected, res.json()['code'])  # 这里的self怎么用？复盘复盘复盘！！！
        except AssertionError as e:
            print("断言错误的是：{}".format(e))
            raise e

# if __name__ == '__main__':
#     unittest.main()


