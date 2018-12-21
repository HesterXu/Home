# -*- coding: utf-8 -*-
# @Time     : 2018/12/11/15:07
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : class_02_webdriver_20181211.py
# @Software : PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/Simple-Small/p/10065674.html")

driver.quit()

