# -*- coding: utf-8 -*-
# @Time     : 2018/12/7/16:22
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson17_do_pandas_01_20181203.py
# @Software : PyCharm

# https://www.cnblogs.com/liulinghua90/p/9935642.html

import pandas as pd

df = pd.read_excel('python12.xlsx',sheet_name = 'Sheet1')  # 打开excel，sheet表单
res = df.values          # 读取所有数据
res_2 = df.ix[0].values  # 读取指定行，ix是index  # pandas自动把第一行作为表头，从0开始读取数据
print(res)
print(res_2)

# 读取行的数据
print(df.ix[[1,2]].values)  # 读取第1行，第2行的数据
# 读取列的数据
print(df['B'].values)      # 读取第B列的数据


