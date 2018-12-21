# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/15:13
# @Author   : Hester Xu
# @Email     : xuruizhu@yeah.net
# @File     : request.py
# @Software : PyCharm

# 写一个http请求的类
import requests
class Http_Request:   # 驼峰命名
    def http_request(self,url,param,http_method,cookies = None):  # param??? params???
        if http_method == 'get':
            res = requests.get(url,param,cookies = cookies)  # cookies=cookies ???
        else:
            res = requests.post(url,param,cookies=cookies)
        return res

