# -*- coding: utf-8 -*-
# @Time     : 2018/11/19/20:07
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson11_object_20181119.py
# @Software : PyCharm
'''
# 写一个机器人类，具有的属性：制造年月 名字
# 第一代机器人：简单交流 直线行走遇到障碍物就会报警 停止行走
# 听歌名 去音乐库找到音乐   然后播放
'''
class RobotOne:
    birthday = '20181119'
    name = 'hester'
    def talk(self):
        print("可以跟你进行简单交流")
    @classmethod
    def walk(cls):
        print("会直线行走")
    def sing(self):
        print("会播放音乐")



















# 对象拥有类里面的所有属性和方法（三种方法）使用权，可以随时调用


'''
    def __init__(self,birthday,name,*args,kargs): #初始化函数,创建对象的时候去传值
        self.birthday = birthday
        self.name = name
        self.hobby = args
        self.kargs = kargs
# 函数里面：动态参数-元组， 关键字参数-字典

    def talk(self):  # 对象方法,self就是对象本身
        print(self.name+"可以跟你进行简单交流") # 对象调用属性
        print(RobotOne.name+"可以跟你进行简单交流")  # 类名调用属性
        print(self.name,'业余爱好是:',self.hobby)
        print(self.name, '业余爱好是:', self.kwargs)
'''

'''
    @classmethod   # 类方法很少用
    def walk(cls): # 类方法，cls就是类名
        print("会直线行走")
    @staticmethod   # 静态方法可以调用属性，一般不用这个，用了最好用对象方法
    def sing(music='00000'):  # 静态方法，和普通函数一样
        print("会播放音乐"+music)
    @staticmethod
    def math_method(a,b):  # 当你的方法里，不需要用到类的属性值时候，可以写成静态方法
        print(a+b)
'''
'''
# 类外面调用对象方法：创建实例对象， 对象调用对象方法
# 创建对象   类名（）
# 对象拥有类里面的所有属性和方法（三种方法）使用权，可以随时调用
r1 = RobotOne()  # 创建对象
r1.sing()   # 对象调用对象方法
r1.talk()
r1.walk()
print(r1.name) # 对象可以调用类里面的方法，属性值
print("======这是分割线=======")
r2 = RobotOne()
r2.sing()
print(r2.birthday)
'''
'''
# 类外面调用类方法： 对象调用 类名称调用
print("======这是分割线=======")
r3 = RobotOne()
r3.walk()
print("======这是分割线=======")
RobotOne.walk()
'''

'''
# 类外面调用静态方法： 对象调用 类名称调用
r4 = RobotOne()
r4.sing()
print("======这是分割线=======")
RobotOne.sing()
'''

'''
# 属性： 类名 和 对象 都可以调用
print(RobotOne.name)
print(RobotOne.birthday)
'''

'''
# 类里面对属性进行调用-----类和对象都可以调用属性
r5 = RobotOne()
r5.talk()
r5.sing()
'''

'''
初始化函数
r5 = RobotOne('20181230','333')
r5.talk('你好哈哈哈哈')
'''

















