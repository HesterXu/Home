# -*- coding: utf-8 -*-
# @Time     : 2018/12/7/20:07
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson19_ddt_01_20181207.py
# @Software : PyCharm

import unittest
from ddt import ddt,data,unpack

test_data = ((3,(1,2)),
             (6,(3,4)))
test_data_2 = [{'a':1,'b':8},
               {'a':6,'b':12}]

@ddt # 装饰测试类
class TestMath(unittest.TestCase):

    @data(*test_data)   # 装饰测试方法    拆出来几个元素，就有几条用例
    @unpack   # 对data拆分出来的数据再次进行拆分， 要用等量的变量来接收 按逗号拆分
    def test_001(self,a,b):  # item是个变量名
        print('a：',a)
        print("b：",b)
        print("--------111---------")

    @data(*test_data_2)
    def test_002(self,item):
        print("item：",item)
        print("a+b={}".format(item['a']+item['b']))
        print("----------222----------")

    @data(*test_data_2)
    @unpack   # 如果拆分的是字典，用来接收数据的变量名必须和字典的key一致 无顺序要求
    def test_003(self,a,b):
        print('a: ',a)
        print('b: ',b)
        print("a+b={}".format(a+b))
        print("----------333----------")

