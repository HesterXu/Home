# -*- coding: utf-8 -*-
# @Time     : 2018/12/24/16:54
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @Software : PyCharm
# @File     : zc.py
# @Function : 正则

import re

# s = '{"mobilephone":"13537821056","pwd":"123456"}'  # 目标字符串
# pattern = '\d{11}'
# res = re.findall(pattern=pattern,string=s) # ['13537821056']
# mobilephone = res[0]
# print(mobilephone)  #  13537821056  <class 'str'>
# s_new = s.replace(mobilephone, '13537821057')
# print(s_new)

s = '{"mobilephone":"${register}","pwd":"123456"}'  # 目标字符串
pattern = '\$\{(.*?)\}'
register = 13537821056
res = re.findall(pattern=pattern,string=s)
print(res)

