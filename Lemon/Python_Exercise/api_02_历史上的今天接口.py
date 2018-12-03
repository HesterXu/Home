# -*- coding: utf-8 -*-
# @Time     : 2018/12/3/15:26
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : api_02_历史上的今天接口.py
# @Software : PyCharm

import requests

# 事件列表
url = 'http://api.juheapi.com/japi/toh'
# url = 'http://api.juheapi.com/japi/tohdet?key=796622b2cd0e707ab77765d8f3e0c636&v=1.0&id=4847'

key = '796622b2cd0e707ab77765d8f3e0c636'
v = 1.0
month = 12
day = 3
params = {v:1.0,month:12,day:3,key:'796622b2cd0e707ab77765d8f3e0c636'}

data = {key:'796622b2cd0e707ab77765d8f3e0c636',v:1.0,month:8,day:3}
res = requests.get(url,params)
print("1:",res.headers)
print("2:",res.text)
print("3:",res.status_code)
print("4:",res.json())
print("5:",res.cookies)

