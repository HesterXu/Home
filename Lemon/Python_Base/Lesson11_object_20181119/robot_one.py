# -*- coding: utf-8 -*-
# @Time     : 2018/11/19/21:38
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : robot_one.py
# @Software : PyCharm

class RobotOne:
    def __init__(self, birthday, name):  # 初始化函数,创建对象的时候去传值
        self.birthday = birthday
        self.name = name
    def walk(self):
        print("会直线行走")
    def talk(self,content):
        print(self.name + "可以跟你进行简单交流，说指定的内容："+content)
        self.walk()
    @staticmethod
    def sing(music='隐形的翅膀'):
        print("会播放音乐" + music)

p = RobotOne('20181111','hester')
p.talk('好好学习,天天向上')

