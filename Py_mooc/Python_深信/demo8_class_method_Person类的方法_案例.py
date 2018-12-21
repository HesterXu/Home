# -*- coding: utf-8 -*-
# @Time     : 2018/11/20/21:55
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : demo8_class_method_Person类的方法_案例.py
# @Software : PyCharm

class Person:
    name = 'Andy'
    gender = 'female'
    age = 20

    def instanceShow(self):
        print(self.name,self.gender,self.age)  # 对象调用属性

    @classmethod
    def classShow(cls):
        print(cls.name,cls.gender,cls.age)    # 类名调用属性

    @staticmethod
    def staticShow():
        print(Person.name,Person.gender,Person.age)  # 类名调用属性

p = Person()
p.instanceShow()   # 实例对象调用实例/对象方法
p.classShow()      # 对象调用类方法
p.staticShow()     # 对象调用静态方法

Person.classShow()  # 类名调用类方法
Person.staticShow() # 类名调用静态方法



