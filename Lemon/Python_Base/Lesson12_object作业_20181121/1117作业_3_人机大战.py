# -*- coding: utf-8 -*-
# @Time     : 2018/11/22/19:37
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : 1117作业_3_人机大战.py
# @Software : PyCharm
'''
3.人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色 1曹操 2张飞 3刘备
2）函数2：角色猜拳  1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个 1-3 的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
'''


'''
class HumanVsPC:
# 第1种方法： if...else... 最简单，必须掌握！！！
    def choose_role(self):
        role_num = input("选择角色(1曹操 2张飞 3刘备)：")
        if role_num == '1':
            # print("你选择的角色是：曹操")
            role_name = "曹操"
        elif role_num == '2':
            # print("你选择的角色是：张飞")
            role_name = "张飞"
        elif role_num == '3':
            # print("你选择的角色是：刘备")
            role_name = "刘备"
        else:
            role_name = "输入数字错误！"
        print("你选择的角色是：{}".format(role_name))
'''

'''  
class HumanVsPC:
# 第2种方法：try...except...  错误处理机制，单元测试要用！！！
    def choose_role(self):
        role_dict = {'1': '曹操', '2': '张飞', '3': '刘备'}
        role_num = input("选择角色(1曹操 2张飞 3刘备)：")
        try:
            role_name = role_dict[role_num]
        except Exception as e:
            print("输入数字错误:",e, "默选认择角色：曹操")
            role_name = '曹操'
        print("选择的角色是：{}".format(role_name))
'''
import random
class HumanVsPC:
# 第3种方法：while
    def choose_role(self):
        role_dict = {'1': '曹操', '2': '张飞', '3': '刘备'}
        role_num = input("选择角色(1曹操 2张飞 3刘备)：")
        while role_num not in role_dict.keys():
            role_num = input("输入数字错误！请重新选择角色(1曹操 2张飞 3刘备)：")
        print("选择的角色是：{}".format(role_dict[role_num]))
        return role_dict[role_num]                # 注意：没有return的话，返回：None ！！！

    def human_fist(self):
        fist_dict = {'1': '剪刀', '2': '石头', '3': '布'}
        fist_num = input("角色出拳(1剪刀 2石头 3布)：")
        while fist_num not in fist_dict.keys():
            fist_num = input("输入数字错误！请重新出拳(1剪刀 2石头 3布)：")
        print("角色出拳是：{}".format(fist_dict[fist_num]))
        return fist_num

    def pc_fist(self):
        fist_dict = {'1': '剪刀', '2': '石头', '3': '布'}
        fist_num = random.randint(1,3)
        print("电脑出拳：{}".format(fist_dict[str(fist_num)]))
        return fist_num

    def human_vs_pc(self):   # self 调用对象方法
        role_name = self.choose_role()  # 角色名
        role_win = 0
        pc_win = 0
        tie = 0
        while True:
            # 角色出拳
            human_fist = int(self.human_fist())    # 调用human_fist()
            # 电脑出拳
            pc_fist = self.pc_fist()       # 调用pc_fist()
            if human_fist - pc_fist == -2 or  human_fist - pc_fist == 1:
                print("角色{}赢了！".format(role_name))
                role_win += 1
            elif pc_fist - human_fist in (-2,1):
                print("电脑赢了！")
                pc_win += 1
            else:
                print("平局！")
                tie += 1
        # 提示用户是否继续
            choice = input("是否继续(y:继续, n:退出):")
            if choice == 'y':
                continue
            else:
                break
        print("角色{}赢{}次，电脑赢{}次，平局{}次".format(role_name,role_win,pc_win,tie))

if __name__ == '__main__':
    game = HumanVsPC()
    game.human_vs_pc()


'''
    def role_fist(self):
        fist_dict = {'1':'剪刀','2':'石头','3':'布'}
        fist_num = input("角色猜拳（1剪刀 2石头 3布）：")
        print("角色{}出拳的是：{}".format(self.role_num,fist_dict[fist_num]))
    
    def role_fist(self):
         fist_num = input("角色猜拳，玩家输入一个1-3的数字（1剪刀 2石头 3布）：")
         if fist_num == '1':
             print("角色猜拳是：剪刀")
         elif fist_num == '2':
             print("角色猜拳是：石头")
         elif fist_num == '3':
             print("角色猜拳是：布")
         else:
             print("角色猜拳，请玩家重新输入一个1-3的数字（1剪刀 2石头 3布）：")
        return int(fist_num)
'''







