# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 17:33
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : demo6_class_method_类方法.py
# @Software: PyCharm

# 对象可以调用 对象方法、类方法、静态方法；类名称可以调用 类方法、静态方法
# 类方法

'''
class Person:
    age = 20
    @classmethod
    def show(cls):
        print(cls.age)
p = Person()
# 类方法使用@classmethod来修饰，而且第一个参数一般命名为cls（也可以是其他名称）
# 类方法通常使用类名称来调用，例如：Person.show()
# 类方法也可以使用实例对象来调用，例如：p.show()
# 类方法调用时，两种调用都是会向它的第一个参数传递类名称
# 不同点：实例方法/对象方法被调用时，要向它的第一个参数传递实例对象
'''

'''
class Person:
    __name = 'hester'
    __age = 12
    @classmethod
    def show(cls):
        print(cls.__name,cls.__age)
Person.show()  # hester 12  调用时向参数cls传递类名称Person， Person.__name, Person.__age
p = Person()
p.show()       # hester 12  调用时向参数cls传递类名称Person,  Person.__name, Person.__age
'''

class Person:
    name = 'a'
    @classmethod
    def show(cls):
        print(cls)   # <class '__main__.Person'>
        print(cls.name)
p = Person()
Person.show() # <class '__main__.Person'>  a  类名调用 类方法，调用时向参数cls传递类名称Person
p.show()      # <class '__main__.Person'>  a  实例对象调用 类方法，调用时向参数cls传递类名称Person










