# -*- coding: utf-8 -*-
# @Time     : 2018/12/20/7:47
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @File     : learn_json.py
# @Software : PyCharm
# @Function : 学习json

import json  # 导入json模块

# # 使用简单的json.dumps()方法对简单数据类型进行编码
# obj = [123,123.123,'abc',[1,2,3],{'key1':(1,2,3),'key2':(4,5,6)},(2,4,'hunt')]
# print("obj是：{}，数据类型是：{}".format(obj,type(obj)))
# print("obj经过repr之后是：{}，数据类型是：{}".format(repr(obj),type(repr(obj))))
# encodedjson = json.dumps(obj)
# print("obj经过encode之后是：{}，数据类型是：{}".format(encodedjson,type(encodedjson)))  # encodedjson ：<class 'str'>
# # 通过输出的结果可以看出，简单类型通过encode之后跟其原始的repr()输出结果非常相似，但是有些数据类型进行了改变
# # 例如上例中的元组则转换为了列表
# # json.dumps()方法返回了一个str对象encodedjson
#
# # 我们接下来对encodedjson进行decode，得到原始数据，需要使用的json.loads()函数
# decodejson = json.loads(encodedjson)
# print("encodedjson经过decode之后是：{}，数据类型是：{}".format(decodejson,type(decodejson)))
# print(decodejson[4]['key1'])
# # loads方法返回了原始的对象，但是仍然发生了一些数据类型的转化。比如，上例中‘abc’转化为了unicode类型。

"""
编码：把一个Python对象编码转换成Json字符串   json.dumps()
解码：把Json格式字符串解码转换成Python对象   json.loads()
"""

s = json.loads('{"name":"test","type":{"name":"seq","parameter":["1","2"]}}')
print(s.keys())  # dict_keys(['name', 'type'])
print(s["name"])  # test
print(s["type"])  # {'name': 'seq', 'parameter': ['1', '2']}
print(s["type"]["name"])   # seq

data = {'a':123,'b':[1,2]}
print(type(data))  # <class 'dict'>
a1 = json.dumps(data)  # json.dumps() 把一个Python对象编码转换成Json字符串
print(type(a1))        # <class 'str'>
a2 = json.loads(a1)    # json.loads() 把Json格式字符串解码转换成Python对象
print(type(a2))        # <class 'dict'>

"""排序"""
data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1,sort_keys=True)
d2 = json.dumps(data2)  # 字典转为字符串
d3 = json.dumps(data2,sort_keys=True)
print(d1,type(d1))  # {"a": 123, "b": 789, "c": 456}
print(d2,type(d2))  # {"b": 789, "a": 123, "c": 456}
print(d3,type(d3))  # {"a": 123, "b": 789, "c": 456}
print(data1==data2)  # True
print(d1==d3)  # True
print(d1==d2)  # False
print(d2==d3)  # False

"""缩进参数"""
data3 = {'b':789,'c':456,'a':123}
d4 = json.dumps(data3,sort_keys=True,indent=4)
print(d4)


