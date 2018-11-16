# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 16:53
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : Lesson5_homework_review_20181105.py
# @Software: PyCharm

'''
1. 寻找10到12岁的小女孩加入球队（包含10，12），询问用户的性别（男：m），（女：f）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
'''
count = 0
for i in range(3):
    gender = input("请输入用户的性别(男:m,女:f)：")
    age = eval(input("请输入用户的年龄："))
    if gender in 'f':
        if 10 <= age <= 12:
            print("这个用户可以加入球队")
            count+=1
        else:
            print("这个用户不可以加入球队")
    else:
        print("这个用户不可以加入球队")
print("满足条件的总人数是{}人".format(count))
