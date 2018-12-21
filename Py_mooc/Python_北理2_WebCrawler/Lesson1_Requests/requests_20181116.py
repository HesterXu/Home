# -*- coding: utf-8 -*-
# @Time     : 2018/11/16/19:51
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : requests_20181116.py
# @Software : PyCharm

import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
print(type(r))
print(r.headers)
r.encoding = 'utf-8'
print(r.text)

r.status_code  #2HTTP请求的返回状态，00连接成功，4040失败
r.text   #HTTP相应内容的字符串形式，即：url对应的页面内容
r.encoding
r.apparent_encoding
r.content

#  Requests库的7个主要方法
requests.request()
requests.get()
requests.head()
requests.post()
requests.put()
requests.patch()
requests.delete()

#  Requests库的异常
requests.ConnectionError
requests.HTTPError
requests.URLRequired
requests.TooManyRedirects
requests.ConnectTimeout
requests.Timeout

r.raise_for_status()  #如果状态不是200，引发HTTPError异常

