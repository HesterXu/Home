# -*- coding: utf-8 -*-
# @Time     : 2018/12/7/16:21
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson17_do_pandas_02_20181203.py
# @Software : PyCharm

# 导入pandas模块：
import pandas as pd

# 读取Excel文件的两种方式：
# 方法一：默认读取第一个表单
df = pd.read_excel('lemon.xlsx') # 这个会直接默认读取到这个Excel的第一个表单
data = df.head()                  # 默认读取前5行的数据
print("获取到的所有值：\n{}".format(data))



