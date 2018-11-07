# -*- coding: utf-8 -*-
# @Time     : 2018/11/7/20:06
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson5_homework1.py
# @Software : PyCharm

'''
1. 寻找10到12岁的小女孩加入球队（包含10，12），询问用户的性别（男：m），（女：f）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
'''
# 第1种方法：
count = 0
for i in range(1,4):
    gender = input("请输入用户的性别(男:m,女:f)：")
    age = eval(input("请输入用户的年龄："))
    if gender == 'f' and 10 <= age <= 12:
        print("这个用户可以加入球队")
        count+=1
    else:
        print("这个用户不可以加入球队")
print("满足条件的总人数是{}人".format(count))

# 第2种方法

# 第3种方法

