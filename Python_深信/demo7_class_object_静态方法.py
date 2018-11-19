# -*- coding: utf-8 -*-
# @Time     : 2018/11/19/19:46
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : demo7_class_object_静态方法.py
# @Software : PyCharm

# 对象可以调用 对象方法、类方法、静态方法；类名称可以调用 类方法、静态方法
# 静态方法
'''
class Person:
    age = 20
    @staticmethod
    def show():
        print(Person.age)
p = Person()
# 静态方法使用@staticmethod来修饰
# 静态方法通常使用类名称或者实例对象来调用，例如：Person.show(), p.show()
# 调用静态方法时，不会向函数传递任何参数
'''

class Person:
    __name = 'hester'
    __age = 12
    @staticmethod
    def show():
        print(Person.__name,Person.__age)
Person.show()  # hester 12   使用类名称或者实例对来调用静态方法
p = Person()
p.show()       # hester 12   使用实例对象来调用静态方法






















