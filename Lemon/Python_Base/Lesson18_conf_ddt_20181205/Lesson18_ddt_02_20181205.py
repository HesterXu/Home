# -*- coding: utf-8 -*-
# @Time     : 2018/12/7/7:24
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson18_ddt_02_20181205.py
# @Software : PyCharm

import unittest
from ddt import ddt,data,unpack

test_data_3 = ((1,2,3),(5,6,7),('a',9))
test_data = [(1, 2, 3), (5, 6, 7)]
test_data_2 = [{'param':{'mobilephone': 18688773467, 'pwd': '123456'},'http_method':'get','expected':'10001',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},

             {'param':{'mobilephone': 18688773467, 'pwd': '123456789'},'http_method':'post','expected':'20111',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},

             {'param':{'mobilephone': 13522332315, 'pwd': '123456'},'http_method':'get','expected':'20111',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/login'},

             {'param':{'mobilephone': 18688773467, 'amount': '1000'},'http_method':'post','expected':'10001',
              'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'}]

@ddt                       # 装饰unittest类的子类
class TestMath(unittest.TestCase):

    @data(*test_data_2)                   # 装饰测试方法
    def test_001(self,item):   # 测试用例经过data装饰，可以传参数，把test_data拆分出来的数据传给item
        print('url：',item['url'])
        print('param：', item['param'])
        print('http_method：', item['http_method'])
        print('expected：', item['expected'])
        print("-------------------------我是分隔符----------------------------------")
        print()  # 回车

    @data(*test_data_2)             # 1个参数接收，4个元素          # 装饰测试方法
    @unpack                      # 4个参数接收，字典时，接收的名字要和key的名字一样        # 把数据一个个取出来
    def test_002(self,url,param,http_method,expected):   # 测试用例经过data装饰，可以传参数，把test_data传给item
        print('url：',url)
        print('param：',param)
        print('http_method：',http_method)
        print('expected：',expected)
        print("-------------------------我是分隔符----------------------------------")
        print()  # 回车

    @data(*test_data)  # 决定有几条用例
    @unpack      # 加unpack之前是两条用例，两个数据：(1, 2, 3)和(5, 6, 7)。
                 # 加了unpack后，对每个数据进行拆分：1，2，3  和 5，6，7
    def test_003(self,a,b,c):
        print('a:',a)
        print('b:',b)
        print('c:',c)
        print('-----------------')

    @data(*test_data_3)  # 决定有几条用例
    @unpack
    def test_004(self,x=None,y=None,z=None):
        print('x:',x)
        print('y:',y)
        print('z:',z)
        print('-------break----------')
