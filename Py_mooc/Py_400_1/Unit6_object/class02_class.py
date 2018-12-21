# -*- coding: utf-8 -*-
# @Time     : 2018/11/22/7:12
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : class02_class.py
# @Software : PyCharm

class Student:    #类名一般首字母大写，多个单词采用驼峰原则
    def __init__(self,name,score):  # 构造方法/初始化函数
        self.name = name
        self.score = score
    def say_score(self):
        print("{}分数是：{}".format(self.name,self.score))

s1=Student("hester",18)
s1.say_score()   # 把s1的内存地址/对象传给say_score的self。
'''
__new__()方法：用于创建对象，一般无需重新定义该方法
__init__()方法：初始化创建好的对象，初始化是给实例属性赋值。
'''
# 一个python对象包含：
# 1.id（identify识别码）
# 2.type（对象类型）
# 3.value（对象的值）：属性（attribute），方法（method）

# __init__()  self指的是刚刚创建好的实例对象
