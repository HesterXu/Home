# -*- coding: utf-8 -*-
# @Time     : 2018/11/23/20:29
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : unit_test_02.py
# @Software : PyCharm

import unittest      # 导入unittest库，python自带的
from Lemon.Python_Base.Lesson13_unit_test_20181123.sai import Sai

class TestNicky(unittest.TestCase):     # 继承unittest库里面的TestCase类
    # 1.用例是一个个的对象方法  2.必须以test开头 3.用例里面不能传递参数
    # 测试Nicky的跑步
    def test_run(self):    # 对象方法，以test开头
        expected = 1000
        actual = 500
# 对比结果 - 断言
        print("hester期望跑{}，实际跑{}".format(expected,actual))
    def test_cooking(self):
        expected = '满汉全席'
        actual = '煮面'
        print("hester期望{}，实际{}".format(expected,actual))

class TestSai(unittest.TestCase):     # 继承unittest库里面的TestCase类
    def test_add_two_positive(self):
        actual = Sai().add(5,6)
        expected = 11
        # 断言去比较结果
        self.assertEqual(expected,actual)

    def test_add_two_negative(self):
        Sai().add(-2,-4)
    def test_add_two_zero(self):
        Sai().add(0,0)














