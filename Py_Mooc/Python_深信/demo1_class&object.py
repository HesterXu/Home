# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 17:06
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : demo1_class&object.py
# @Software: PyCharm

class Person:  # 定义了一个Person类
    name = 'Hester'  # 定义了一个属性
    def printName(self):
        print(self.name)  # 定义了一个方法
p = Person() # 产生了一个Person的实例对象。实例对象是根据类的模板生成的一个内存实体，有确定的数据与内存地址。


class Person:
    name = 'hester'
    age = 20
# 1. 读取访问 类的属性
print(Person.name,Person.age) #使用类的名称 访问类的属性
p = Person()
print(p.name,p.age)    # 使用类的实例对象 访问类的属性

# 2. 改变 类的属性
Person.name = 'xxx'   #只能通过类的名称改变类的属性
print(Person.name,Person.age)

p = Person()    #不能通过对象改变类的属性
p.name = 'yyy'
print(Person.name,Person.age)
