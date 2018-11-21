# -*- coding: utf-8 -*-
# @Time     : 2018/11/20/22:31
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : demo9_object_init.py
# @Software : PyCharm

# 构造与析构函数:

# 1. 构造方法__init__(self,...) 在生成对象时调用,可以用来进行一些初始化操作,不需要显示去调用,系统会默认去执行.
# 如果用户自己没有重新定义构造方法,系统就会自动执行默认的构造方法.
# 2. 析构方法__del__(self) 在释放对象时调用,可以在里面进行一些释放资源的操作,不需要显示调用.

class Person1:
    def __init__(self,n,g,a):
        self.name = n
        self.gender = g
        self.age = a
p = Person1('hester','Male',20)
print(p.name,p.gender,p.age)
# print(Person.name,Person.age)  # AttributeError: type object 'Person' has no attribute 'name'

class Person2:
    def __init__(self):
        print("__init__",self)
    def __del__(self):
        print("__del__",self)
q = Person2()
'''
__init__ <__main__.Person2 object at 0x00000000039B8940>
__del__ <__main__.Person2 object at 0x00000000039B8940>
'''
print(q)
'''__init__ <__main__.Person2 object at 0x0000000003AC8908>
<__main__.Person2 object at 0x0000000003AC8908>
__del__ <__main__.Person2 object at 0x0000000003AC8908>
'''














