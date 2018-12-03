# -*- coding: utf-8 -*-
# @Time     : 2018/12/3/15:24
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : api_01_新闻头条接口.py
# @Software : PyCharm


# 接口地址：http://v.juhe.cn/toutiao/index
# 返回格式：json
# # 请求方式：get/post
# # 请求示例：http://v.juhe.cn/toutiao/index?type=top&key=APPKEY
# # 接口备注：返回头条，社会，国内，娱乐，体育，军事，科技，财经，时尚等新闻信息
#
# # 请求参数：type=yule&key=e636f83574af418cbacfd5f01c104bab

import requests
url1 = 'http://v.juhe.cn/toutiao/index?type=yule&key=e636f83574af418cbacfd5f01c104bab'

res1 = requests.get(url1)
print("1:",res1.headers)
print("2:",type(res1.text),res1.text)
print("3:",type(res1.json()),res1.json())
print("4:",res1.status_code)
print("5:",res1.cookies)

