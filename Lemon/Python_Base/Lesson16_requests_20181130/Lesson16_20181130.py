# -*- coding: utf-8 -*-
# @Time     : 2018/11/30/20:05
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson16_20181130.py
# @Software : PyCharm


import requests

url = 'http://lemfix.com/topics/25'

res = requests.get(url)

res2 = requests.post(url)

