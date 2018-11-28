# -*- coding: utf-8 -*-
# @Time     : 2018/11/28/20:05
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson15_20181128.py
# @Software : PyCharm


# 3.cookie session
# cookie：在客户端 存储用户的一些数据 比如说用户名啥的浏览记录
# session：在服务器端 记录用户的请求状态，一般默认时间是30min'

# 会员卡机制
# session_id会存在cookie中，每次请求cookie中的所有信息都会传送给服务器，服务器通过sessin_id
# 来识别是否是同一个用户的请求。
# 不是同一个用户的话，就会要求用户重新登陆。

# http请求是无状态的

# 4.剖析访问授权
# 鉴权：访问的接口是否正常，是否是非法访问，绕过前端访问  token
# 授权：是否具有访问接口的权限  key
# 一般来收，是唯一的，全局的，动态的，具备一定特征
# 验签：













