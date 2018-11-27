# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 10:26
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : unittest_homework_20181126.py
# @Software: PyCharm

'''
1：自己写一个工具类，完成数学的加减乘除以及平方积操作。
2：对每个方法写2个用例。
3：针对测试用例选用不同的方法去执行，然后生成测试报告。
下一节课内容：cookie session token key 以及工具的使用！
'''

import unittest
from Lemon.Python_Base.Lesson14_unittest_http_20181126.myclass_homework_20181126 import MathTool

class mytest(unittest.TestCase):

    def setUp(self):     # 初始化工作
        print("do something before test.Prepare environment.")
    def tearDown(self):  # 退出清理工作
        print("do something after test.Clean up.")

    # 具体的测试用例，一定要以test开头
    """Test method sum(a, b)"""
    def test_sum_01(self):   # 测试加法pass   一个TestCase的实例就是一个测试用例
        print("测试加法pass")
        self.assertEqual(3,MathTool().sum(1,2),'test sum pass')
    def test_sum_02(self):   # 测试加法fail
        print("测试加法fail")
        self.assertNotEqual(11,MathTool().sum(1,2),'test sum fail')

    def test_sub_01(self):      # 测试减法pass
        print("测试减法pass")
        self.assertEqual(2,MathTool().sub(3,1),'test sub pass')
    def test_sub_02(self):      # 测试减法fail
        print("测试减法fail")
        self.assertNotEqual(3,MathTool().sub(3,1),'test sub fail')

    def test_mul_01(self):      # 测试乘法pass
        print("测试乘法pass")
        self.assertEqual(6,MathTool().mul(2,3),'test mul pass')
    def test_mul_02(self):      # 测试乘法fail
        print("测试乘法fail")
        self.assertNotEqual(5,MathTool().mul(2,3),'test mul fail')

    def test_div_01(self):      # 测试除法pass
        print("测试除法pass")
        self.assertEqual(3,MathTool().div(6,2),'test div pass')
    def test_div_02(self):      # 测试除法fail
        print("测试除法fail")
        self.assertNotEqual(2,MathTool().div(6,2),'test div fail')

    def test_squ_01(self):      # 测试平方积pass
        print("测试平方积pass")
        self.assertEqual(36,MathTool().squ(2,3),'test squ pass')
    def test_squ_02(self):      # 测试平方积fail
        print("测试平方积fail")
        self.assertNotEqual(20,MathTool().squ(2,3),'test squ fail')














