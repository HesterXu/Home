# -*- coding: utf-8 -*-
# @Time    : 2018/11/19 17:32
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : demo5_class_method_对象方法.py
# @Software: PyCharm

# 对象可以调用 对象方法、类方法、静态方法；类名称可以调用 类方法、静态方法
# 实例方法/对象方法
'''
class Person:
    age = 20
    def show(self):
        print(self.age)
p = Person()
# 实例方法/对象方法 至少有一个参数，一般以名为self的变量作为该参数（也可以是其他名称）
# 实例方法/对象方法 通过实例对象来调用，例如：p.show()
# 如果使用类名称调用，需要人为传递实例参数，例如：Person.show(p)
# 实例方法/对象方法被调用时，要向它的第一个参数传递实例对象
'''

'''
class Person:
    name = 'hester'
    age = 12
    def getName(self):  # 实例方法/对象方法
        return self.name
    def getAge(self):  # 实例方法/对象方法
        return self.age
p = Person()
print(p.getName(),p.getAge())  # hester 12  通过实例对象来调用 实例方法/对象方法
'''

'''
class Person:
    name = 'a'
    def show(self):   # 实例方法/对象方法
        print(self)
p = Person() # 实例对象
print(p)       # <__main__.Person object at 0x0000000002787E48>
p.show()       # <__main__.Person object at 0x00000000021E7E48>  p实例对象传递给self
Person.show(p) # <__main__.Person object at 0x0000000001EE7F98>
'''

'''
class Person:
    name = 'a'
    def show(self,s):   # 实例方法/对象方法
        print(self,s)
p = Person() # 实例对象
print(p)               # <__main__.Person object at 0x0000000002787E48>
p.show('hi')           # <__main__.Person object at 0x00000000021E7E48>   hi     hi传给s
Person.show(p,'hello') # <__main__.Person object at 0x0000000001EE7F98>   hello  hello传给s
'''




