# -*- coding: utf-8 -*-
# @Time     : 2018/11/30/20:44
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson16_03.py
# @Software : PyCharm

import requests

login = 'http://47.107.168.8807:80/futureloan/mvc/api/member/login'
login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
# 发送一个get请求
login_res = requests.get(login,login_data)
# 看登陆的响应头
print(login_res.headers)
# 看登陆的相应正文
print(login_res.text,type(login_res.text))
print(login_res.json(),type(login_res.json()))
# 看登陆的状态码
print(login_res.status_code)
print(login_res.cookies)
print(login_res.cookies['JSESSIONID'])
print("-----------------------------------------------------------------")
# 登陆成功之后发起充值请求
recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
recharge_data={'mobilephone':18688773467,'amount':'1000'}
recharge_res = requests.post(recharge,recharge_data,cookies = login_res.cookies)

# 看充值响应正文
print(recharge_res.json())


