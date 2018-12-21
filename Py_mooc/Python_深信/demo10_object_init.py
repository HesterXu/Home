# -*- coding: utf-8 -*-
# @Time     : 2018/11/20/23:03
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : demo10_object_init.py
# @Software : PyCharm

# 对象初始化
# 构造函数中设置默认参数
class Person:
    def __init__(self,n="123",g="male",a=0):
        self.name = n
        self.gender = g
        self.age = a
    def show(self):
        print(self.name,self.gender,self.age)
a = Person("hester")
b = Person('hester','female')
c = Person('hester','female',20)
d = Person()
a.show()
b.show()
c.show()
d.show()
