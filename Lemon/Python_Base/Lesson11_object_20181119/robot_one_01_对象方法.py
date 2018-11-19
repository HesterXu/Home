# -*- coding: utf-8 -*-
# @Time     : 2018/11/20/7:38
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : robot_one_01_对象方法.py
# @Software : PyCharm
'''
# 写一个机器人类，具有的属性：制造年月 名字
# 第一代机器人：简单交流 直线行走遇到障碍物就会报警 停止行走
# 听歌名 去音乐库找到音乐   然后播放
'''

# 1创建对象；# 2..对象调用对象方法；# 3.对象调用属性；# 4.类名调用属性
class RobotOne:
    birthday = '20181119'
    name = 'hester'
    def talk(self):  # 对象方法/实例方法
        print("可以跟你进行简单交流")
    def walk(self):
        print("会直线行走")
    def sing(self):
        print("会播放音乐")

# 1.创建对象：类名（）
r1 = RobotOne()
# 2.对象调用对象方法
r1.sing()
r1.talk()
r1.walk()
print("======1======")
# 3.对象调用属性
print(r1.name)
print(RobotOne().name)
print("======2======")
# 4.类名调用属性
print(RobotOne.name)
print(RobotOne.birthday)

