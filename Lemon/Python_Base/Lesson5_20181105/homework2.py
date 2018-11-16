# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 11:12
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : homework3.py
# @Software: PyCharm

# 2. 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序： 冒泡排序：小的排前面，大的排后面。
a=[1,7,4,89,34,666,99,8,2,2]
for i in range(1, len(a)):
    for j in range(len(a)-i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
