# -*- coding: utf-8 -*-
# @Time     : 2018/11/21/19:03
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson12_object_20181121.py
# @Software : PyCharm

class HumanVsPC:
    def role(self):  #选择角色
        '''
        role_num = input("请选择角色：1曹操 2张飞 3刘备")
        print("你选择的角色是：")

        if role_num == '1':
            role = '曹操'
        elif role_num == '2':
            role = '张飞'
        elif role_num == '3':
            role = '刘备'
        else:
            role = "输入的数字错误"
        '''
        role_dict={'1':"曹操",'2':"张飞",'3':"刘备"}
        role_num = input("请选择角色：1曹操 2张飞 3刘备")
        print("你选择的角色是：{}".format(role_dict[role_num]))
        try:
            print("")
        except Exception as e:
















