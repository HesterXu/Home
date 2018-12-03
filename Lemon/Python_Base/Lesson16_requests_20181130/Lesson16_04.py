# -*- coding: utf-8 -*-
# @Time     : 2018/11/30/21:17
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson16_04.py
# @Software : PyCharm

# 了解即可-- 一个会话下，不用cookies
import  requests
#登录
login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
login_data={'mobilephone':18688773467,'pwd':'123456'}
#充值
recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
recharge_data={'mobilephone':18688773467,'amount':'1000'}

# 生成一个会话
s = requests.session()
res_login = s.get(login,params = login_data)
res_recharge = s.get(recharge,params = recharge_data)

print("登陆的结果：",res_login.json())
print("充值的结果：",res_recharge.json())





