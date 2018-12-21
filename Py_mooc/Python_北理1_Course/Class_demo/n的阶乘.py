# -*- coding: utf-8 -*-
# @Time     : 2018/11/6/6:30
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : n的阶乘.py
# @Software : PyCharm

#n的阶乘的递归

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

