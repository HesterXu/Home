# -*- coding: utf-8 -*-
# @Time     : 2018/12/22/6:37
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @Software : PyCharm
# @File     : learn20181221.py
# @Function : 正则表达式完成字符串的查找

import re

# s1 = 'hello world hello'
# pattern = 'hello'

# # match()方法
# res = re.match(pattern=pattern,string=s1) # 只从最开始位置找 # 同search,不过在字符串开始处进行匹配
# print(res)  # <_sre.SRE_Match object; span=(0, 5), match='hello'>

# # findall()方法
# res1 = re.findall(pattern=pattern,string=s1)  # 返回所有满足匹配条件的结果,放在列表里
# print(res1)  # ['hello', 'hello']  <class 'list'>

# # search()方法
# res2 = re.search(pattern=pattern,string=s1) # 从任意位置找，只返回一个
# print(res2)  # <_sre.SRE_Match object; span=(0, 5), match='hello'>
# # 函数会在字符串内查找模式匹配,直到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# # 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

s = '{"mobilephone":"13537821056","pwd":"123456"}'  # 目标字符串
pattern2 = '\d{11}'
res3 = re.findall(pattern=pattern2,string=s) # ['13537821056']
mobilephone = res3[0]
print(mobilephone)  #  13537821056  <class 'str'>
s_new = s.replace(mobilephone, '13537821057')
print(s_new)
