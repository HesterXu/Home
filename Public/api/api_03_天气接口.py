# -*- coding: utf-8 -*-
# @Time     : 2018/12/3/16:15
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : api_03_天气接口.py
# @Software : PyCharm

import requests
weather_url_1 = 'http://t.weather.sojson.com/api/weather/city/101030100'


weather_res_1 = requests.get(weather_url_1)
print(weather_res_1)
print(weather_res_1.text)

# weather_res_2 = requests.get(weather_url_2)
# print(weather_res_2)
# print(weather_res_2.text)
