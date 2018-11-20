# -*- coding: utf-8 -*-
# @Time     : 2018/11/21/7:06
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : demo12_class_inherit.py
# @Software : PyCharm

# 类的派生与继承
# 继承类构造函数： 通过类名称Person直接调用Person的__init__函数，并提供所要的4个参数。
# 继承类是不会自动调用基类的构造函数，必须显示调用。
# Python继承中的一些特点：
# 1.
# 2.
# 3. 先在子类中查找调用的方法，再
class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    def show(self):
        print(self.name,self.gender,self.age,end = "")

class Student(Person):
    def __init__(self,name,gender,age,dept,major):
        Person.__init__(self,name,gender,age)
        self.dept = dept
        self.major = major
    def show(self):
        Person.show(self)
        print(self.dept,self.age)
s = Student('hester','female',20,'computer','software')
s.show()
