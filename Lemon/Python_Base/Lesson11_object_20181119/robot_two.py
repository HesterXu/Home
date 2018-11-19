# -*- coding: utf-8 -*-
# @Time     : 2018/11/19/21:39
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : robot_two.py
# @Software : PyCharm

from Lemon.Python_Base.Lesson11_object_20181119.robot_one import RobotOne
# 类继承
class RobotTwo(RobotOne): # RobotTwo是子类
    def __init__(self,name):
        self.name = name

    def jump(self):  # 拓展  父类没有的函数，只有子类有的函数。
        print("遇到障碍物可以双脚蹦高，跳过")
    def walk(self,km):  # 重写  子类里面跟父类重名的函数叫重写。跟函数内容和参数无关
        print("可以直线行走{}米，遇到障碍绕行".format(km))

r1 = RobotTwo('幸福') # 父类有初始化参数，要传参
r1.jump()
r1.talk('hester  今天真棒')  # 对象方法
r1.sing('七里香')  # 静态方法
r1.walk(111)

# 同名叫重写；不同命叫拓展 -- 针对函数
# 子类有的用子类，没有的用父类


