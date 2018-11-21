# -*- coding: utf-8 -*-
# @Time     : 2018/11/6/21:41
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : 局部变量.py
# @Software : PyCharm
'''
def f(a,b):
  a=4
  return a+b
def main():
  a=5
  b=6
  print(f(a,b),a+b)
main()
'''

def func(a,b):
  c=a**2+b
  b=a
  return c
a=10
b=100
c=func(a,b)+a

print(a,b,c)
