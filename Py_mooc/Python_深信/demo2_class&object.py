# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 17:07
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : demo2_class&object.py
# @Software: PyCharm

# 类属性 与 实例属性

class Person:
    name = 'xxx'  # 定义一些属性
    age = 20
# 使用类名称 读取类属性
print(Person.name,Person.age)
# 使用类名称 改变类属性
Person.name = 'yyy'
Person.age = 21
print(Person.name,Person.age)

# 通过类的对象访问类属性
class Person:
    name = 'xxx'
    age = 20
p = Person()
# 使用对象名称 读取类属性
print(p.name,p.age)

'''
实例有结合任何属性的功能。 对象实例.属性 = ...
如果该对象实例存在这个属性，这个属性值就会被改变；
如果不存在该属性，就会自动为该对象实例创建一个这样的属性。
'''
class Person:
    name = 'xxx'
    age = 20
p = Person()
print(p.name,p.age)   # xxx  20
p.name = 'yyy'    # 这条语句生成p实例的name属性，不同于Person的name属性
p.gender = 'male' # 这条语句生成p实例的gender属性，这是新加的，Person没有gender属性
print(p.name,p.gender,p.age)   # yyy male 20
print(Person.name,Person.age)  # xxx 20

q = Person()
q.id = 111  # 这条语句生成q实例的id属性，这是新加的，Person没有id属性
print(q.name,q.age,q.id)  # xxx 20 111
