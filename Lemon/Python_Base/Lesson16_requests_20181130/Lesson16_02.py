# -*- coding: utf-8 -*-
# @Time     : 2018/11/30/20:34
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson16_02.py
# @Software : PyCharm


import requests

url = 'http://lemfix.com/topics/25'

res = requests.get(url)
print(res)

# response
print(res.headers)
print(res.text)
print(res.status_code)

# request
print(res.request.headers)
print(res.url)

