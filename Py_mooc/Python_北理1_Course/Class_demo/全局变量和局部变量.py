# -*- coding: utf-8 -*-
# @Time     : 2018/11/3/22:25
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : 全局变量和局部变量.py
# @Software : PyCharm

n,s = 10,100
def fact(n):
    s = 1
    #global s
    for i in range(1,n+1):
        s *= i
    return s
print(fact(n),s)
