# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 14:20
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : demo3_class&object.py
# @Software: PyCharm

# 访问权限
class Person:
    name = 'hester'
    age = 20

'''Person中的name和age都是公有的，可以直接在类外通过对象名访问，
如果想定义成私有的，则需在前面加两个下划线 '__'
'''

class Person:
    __name = 'hester'
    age = 12
#print(Person.__name) #错误，Person没有__name这个属性
print(Person.age)     # 12


class Person:
    __name = 'hester'
    age = 12
    def show(self):
        print(self.__name,self.age)
p = Person()
p.show()  # hester 12


class Person:
    __name = 'hester'
    age = 12
    def __show(self): # 类的属性可以是私有，类的方法也可以是私有。
        print(self.__name,self.age)
p = Person()
# p.__show()  #'Person' object has no attribute '__show'


class Person:
    __name = 'hester'
    age = 12
    def __show(self):
        print(self.__name,self.age)
    def display(self):
        self.__show()
p = Person()
p.display()  # hester 12
