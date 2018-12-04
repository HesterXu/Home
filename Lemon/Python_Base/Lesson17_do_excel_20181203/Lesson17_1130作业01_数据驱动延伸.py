# -*- coding: utf-8 -*-
# @Time     : 2018/12/4/21:20
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson17_1130作业01_数据驱动延伸.py
# @Software : PyCharm

'''
写一个http请求的类 然后完成单元测试
1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
'''

# 写一个http请求的类
import requests
class HttpRequest:   # 驼峰命名
    def http_request(self,url,param,http_method,cookies = None):  # param??? params???
        if http_method == 'get':
            res = requests.get(url,param,cookies = cookies)  # cookies=cookies ???
        else:
            res = requests.post(url,param,cookies=cookies)
        return res


