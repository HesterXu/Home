# -*- coding: utf-8 -*-
# @Time     : 2018/11/16/22:40
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : requests_通用代码框架_20181116.py
# @Software : PyCharm

#爬取网页的通用代码框架
import requests
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()   #如果状态不是200，引发HTTPError异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url="http://www.baidu.com"
    print(getHTMLText(url))
