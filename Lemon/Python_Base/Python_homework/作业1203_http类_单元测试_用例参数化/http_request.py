# -*- coding: utf-8 -*-
# @Time     : 2018/12/6/17:08
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : request.py
# @Software : PyCharm


import requests
class HttpRequest:
    def http_request(self,url,param,http_method,a=None):
        if http_method == 'get':
            res = requests.get(url,param,cookies=a)
        else:
            res = requests.post(url,param,cookies=a)
        return res
