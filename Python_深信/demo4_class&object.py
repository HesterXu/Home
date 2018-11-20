# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 14:21
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : demo4_class&object.py
# @Software: PyCharm

# Person类的属性
class Person:  # 编写个人信息类，并建立对象访问属性。
    name = "xxx"   # name，gender，age都是类属性，类属性一般使用类名称Person访问。
    gender = 'x'
    age = 0

p = Person()
print(p.name,p.gender,p.age)      #通过实例对象p访问类属性 xxx x 0
print(Person.name,Person.gender,Person.age)  # 通过类名称Person访问类属性 xxx x 0

p.name = 'A'      # p.name  这三个属性是新产生的实例对象自己的属性，和类属性不同
p.gender = 'Male'
p.age = 20

Person.name = 'B'  # 修改了类属性
Person.gender = 'Female'
Person.age = 21

print(p.name,p.gender,p.age) # 打印p实例对象的属性  A Male 20
print(Person.name,Person.gender,Person.age)  # 打印类属性  B Female 21

