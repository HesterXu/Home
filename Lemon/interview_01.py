# -*- coding: utf-8 -*-
# @Time     : 2018/11/17/14:36
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : interview_01.py
# @Software : PyCharm
'''
# 1、Python里面如何生成随机数
# 生成[0,1）之间的浮点数
import random
print(random.random())
# 生成指定范围的浮点数
print(random.uniform(1,2))
# 生成指定范围的整数
print(random.randint(1,10))
# 指定范围，指定间隔生成随机数
print(random.randrange(10))
print(random.randrange(1,10,2))

# 从序列中获取一个随机元素，参数seq表示序列。
list1 = [1,2,3,'a','this']
print(random.choice(list1))
# 从指定序列中随机获取指定长度的片断
list1 = [1,2,3,'a','this']
print(random.sample(list1,3))
print(random.sample(list1,3))

# 2、字符串逆序输出
# 方法一：
s = "abcdefg"
print(s[::-1])
# 方法二：
s = "abcdefg"
cList = list(s)   # 字符串转为列表
cList.reverse()
print("".join(cList))   #列表转为字符串
# 方法三：
#coding=utf-8
def reverseStr(ss):
  c = []
  for i in range(len(ss)):
    c.append(ss[i])
  c.reverse() # 反转列表
  return ''.join(c)
if __name__ == '__main__':
  s = input("please input str: ")
  print(reverseStr(s))
'''
# 3、判断一个字符串是否为回文字符串
def converted(s):
  ss  = s[:]
  if len(ss) >= 2 and s == ss[::-1]:
    return True
  else:
    return False
if __name__ == "__main__":
  s = "abcdcba"
  print(converted(s))
  print(converted("adgede"))

