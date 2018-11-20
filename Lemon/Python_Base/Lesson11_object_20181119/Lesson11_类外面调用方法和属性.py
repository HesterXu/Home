# -*- coding: utf-8 -*-
# @Time     : 2018/11/20/20:28
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson11_类外面调用方法和属性.py
# @Software : PyCharm

'''
# 写一个机器人类，具有的属性：制造年月 名字
# 第一代机器人：简单交流 直线行走遇到障碍物就会报警 停止行走
# 听歌名 去音乐库找到音乐   然后播放
'''
''' 
类外面 调用方法和属性：
# 1.创建对象；
# 2.对象调用：对象方法；类方法；静态方法
# 3.类名调用：类方法；静态方法
# 4.对象调用：属性
# 5.类名调用：属性
'''
class RobotOne:
    birthday = '20181119'
    name = 'hester'

    def talk(self):     # 对象方法/实例方法
        print("可以跟你进行简单交流")
    @classmethod
    def walk(cls):      #类方法
        print("会直线行走")
    @staticmethod
    def sing():         # 静态方法，和普通函数一样。
        print("会播放音乐")
    @staticmethod
    def math(a,b):     # 静态方法，当方法里面不需要用到类的属性值时，可以写成静态方法。
        print(a+b)

# 1.创建对象r1：类名（）
r1 = RobotOne()
# 2.对象r1调用对象方法,类方法,静态方法
print("======对象r1调用对象方法,类方法,静态方法：======")
r1.talk()   # 对象r1调用对象方法
r1.walk()   # 对象r1调用类方法
r1.sing()   # 对象r1调用静态方法
# 3.创建对象r2：类名（）
r2 = RobotOne()
# 4.对象r2调用对象方法,类方法,静态方法
print("======对象r2调用对象方法,类方法,静态方法：======")
r2.talk()   # 对象r2调用对象方法
r2.walk()   # 对象r2调用类方法
r2.sing()   # 对象r2调用静态方法
# 5.对象RobotOne()调用对象方法,类方法,静态方法
print("======对象RobotOne()调用对象方法,类方法,静态方法：======")
RobotOne().talk()   # 对象RobotOne()调用对象方法
RobotOne().walk()   # 对象RobotOne()调用类方法
RobotOne().sing()   # 对象RobotOne()调用静态方法
# 6.类名调用类方法,静态方法
print("======类名调用类方法,静态方法：======")
RobotOne.walk()     # 类名RobotOne调用类方法
RobotOne.sing()     # 类名RobotOne调用静态方法
# 7.对象r1调用属性
print("======对象r1调用属性：======")
print(r1.name)
print(r1.birthday)
# 8.对象r2调用属性
print("======对象r2调用属性：======")
print(r2.name)
print(r2.birthday)
# 9.对象RobotOne()调用属性
print("======对象RobotOne()调用属性：======")
print(RobotOne().birthday)
print(RobotOne().name)
# 10.类名调用属性
print("======类名调用属性：======")
print(RobotOne.name)
print(RobotOne.birthday)


