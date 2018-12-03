# -*- coding: utf-8 -*-
# @Time     : 2018/12/2/22:35
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : homework_01.py
# @Software : PyCharm
'''
写一个http请求的类 然后完成单元测试
1：利用requests模块，编写一个可以完成http的get请求以及post请求的类。
2：利用登录和充值的两个数据，详情见公告，完成1中编写的类的单元测试（一条龙服务，包含测试报告）
'''
# 被测的类：http请求类
import requests
class Myclass():
    def http_request(self,url,params,http_method,cookies=None):
        if http_method == 'get':
            res = requests.get(url, params, cookies=cookies)
        else:
            res = requests.post(url, params, cookies=cookies)
        return res.json()['msg']


'''
login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
r = Myclass()
res_login = r.http_request(login, login_data, 'get')
print(res_login)
'''
'''
if __name__ == '__main__':
    # 登陆
    login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
    res_login = Myclass().http_request(login, login_data, 'get')
    print("登陆的结果是:", res_login.json())
    print(res_login.json()['msg'])
    # 充值
    recharge = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
    recharge_data = {'mobilephone': 18688773467, 'amount': '1000'}
    res_recharge = Myclass().http_request(recharge, recharge_data, 'post',res_login.cookies)
    print("充值的结果是:", res_recharge.json())
'''
