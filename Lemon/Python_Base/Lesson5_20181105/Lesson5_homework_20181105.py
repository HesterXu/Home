# -*- coding: utf-8 -*-
# @Time     : 2018/11/5/20:47
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson5_homework_20181105.py
# @Software : PyCharm

login_info = {"admin":"root","user_1":"123456"}
while True:
    name = input("请输入用户名：")
    if name not in login_info.keys():
        print("请重新输入正确的用户名：")
    else:
        #
        count = 0
        while True:
            pwd = print("请输入密码：")
            if pwd == login_info[name]:
                print("登陆成功")
                break
            else:
                count += 1
                print("密码错误，还有{}次机会，请重新输入密码：".format(3-count))
                if count == 3:
                   print("用户已被冻结！")
                   break
        break
