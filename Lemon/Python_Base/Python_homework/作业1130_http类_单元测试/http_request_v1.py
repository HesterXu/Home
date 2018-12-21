# -*- coding: utf-8 -*-
# @Time     : 2018/12/6/11:57
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : http_request_v1.py
# @Software : PyCharm

"""1130-写一个http请求的类 然后完成单元测试
1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
温馨提示：可以用到全部变量，global"""

"""疑问，复盘的点：
1.全局变量global用在哪里？？？定义类之前？类里面的函数之前？
2.定义函数时的参数，函数里面的参数？两者异同？？？
3.if__name__=='__main__'函数的作用？它是放在类里面和函数对齐，还是类外面？

"""
import requests
class HttpRequest:
    def http_request(self,url,param,http_method,a=None):
        if http_method == 'get':
            res = requests.get(url,param,cookies=a)
        else:
            res = requests.post(url,param,cookies=a)
        return res



