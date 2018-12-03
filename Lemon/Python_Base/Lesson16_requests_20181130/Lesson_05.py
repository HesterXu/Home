# -*- coding: utf-8 -*-
# @Time     : 2018/12/3/6:22
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson_05.py
# @Software : PyCharm

# 课堂小练习- 写一个http请求
'''
#登录
地址和数据
login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
login_data={'mobilephone':18688773467,'pwd':'123456'}
#充值
地址和数据
recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
recharge_data={'mobilephone':18688773467,'amount':'1000'}
'''

import requests
def http_request(url,params,http_method,cookies = None):
    if http_method == 'get':
        res = requests.get(url,params,cookies = cookies)
    else:
        res = requests.post(url,params,cookies = cookies)
    return res

if __name__ == '__main__':
    # 登陆
    login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
    # 充值
    recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
    recharge_data={'mobilephone':18688773467,'amount':'1000'}

    res_login = http_request(login,login_data,'get')
    print("登陆的结果是:",res_login.json())
    res_recharge = http_request(recharge,recharge_data,'post',res_login.cookies)
    print("充值的结果是:",res_recharge.json())
