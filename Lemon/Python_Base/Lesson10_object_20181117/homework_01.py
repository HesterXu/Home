# -*- coding: utf-8 -*-
# @Time     : 2018/11/17/13:38
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : homework_01.py
# @Software : PyCharm
'''
1：创建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性。
在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；
再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
'''
class User:
    def __init__(self,first_name,last_name,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print("打印用户信息摘要：姓:{},名:{},年龄:{},性别:{}".format(self.last_name,self.first_name,self.age,self.gender))

    def greet_user(self):
        print("{} {},你好！".format(self.last_name,self.first_name))

u1 = User('蕊竹','许',18,'女')
u1.describe_user()
u1.greet_user()
u2 = User('hester','xu',20,'female')
u2.describe_user()
u2.greet_user()
u3 = User('nicky','zhao',22,'male')
u3.describe_user()
u3.greet_user()


