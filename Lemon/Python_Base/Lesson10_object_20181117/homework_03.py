# -*- coding: utf-8 -*-
# @Time     : 2018/11/17/13:35
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : homework_03.py
# @Software : PyCharm

'''
3.人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色 1曹操 2张飞 3刘备
2）函数2：角色猜拳  1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个 1-3 的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
'''

import random
class Game:
    def select_role(self):
        name_dict = {1:"曹操",2:"张飞",3:"刘备"}
        select_role = int(input("请选择角色(1:曹操 2:张飞 3:刘备)："))
        role_name = name_dict[select_role]
        return role_name

    def role_guessing(self):
        role_guessing = int(input("角色猜拳(1剪刀 2石头 3布),请玩家输入一个1-3的数字："))
        return role_guessing

    def machine_guessing(self):
        machine_guessing = random.randint(1,3)
        print("电脑出拳：{}".format(machine_guessing))
        return machine_guessing

    def versus(self):
        winRole = 0
        winMachine = 0
        tie = 0
        while True:
            select_role = self.select_role()
            role_guessing = self.role_guessing()
            machine_guessing = self.machine_guessing()

            if role_guessing == machine_guessing:
                tie += 1
                print("平局")
            elif (role_guessing == 1 and machine_guessing == 3)\
                or (role_guessing == 3 and machine_guessing == 2) \
                or (role_guessing == 2 and machine_guessing == 1):
                winRole += 1
                print("本局{}胜".format(select_role))
            else:
                winMachine += 1
                print("本局电脑胜")

            c = input("是否继续?（y:继续，n:退出）： ")
            if c == 'y':
                continue
            else:
                break
        print("角色赢{}局，电脑赢{}局，平局{}次".format(winRole, winMachine,tie))
        print("游戏结束！")

game = Game()
Game().versus()






















