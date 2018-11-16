# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 11:12
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : homework3.py
# @Software: PyCharm

'''
有一组用户的登录信息存储在字典 login_info 里面，
字典格式如下：login_info={"admin":"root","user_1":"123456"}
key表示用户名，value表示密码，请编写函数满足如下条件：
1）设计1个登陆的程序， 不同的用户名和对成密码存在个字典里面， 输入正确的用户名和密码去登陆，
2）首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名
3)当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应，则提示密码错误请重新输入。
4)如果密码输入错误超过三次，中断程序运行。
5)当输入密码错误时，提示还有几次机会
6)用户名和密码都输入正确的时候，提示登陆成功!
'''

login_info={"admin":"root","user_1":"123456"}
username = input("请输入用户名：")
while username not in login_info.keys() or False:
    username = input("请输入正确的用户名：")

pwd = input("请输入密码：")
def fac(pwd):
    i = 3
    while i <= 3:
        if pwd in login_info[username]:
            print("登录成功")
            break
        elif i == 0:
            break
        print("密码错误，还有{}次机会".format(i))
        pwd = input("请重新输入密码：")
        i -= 1
if pwd in login_info[username]:
    print("登录成功")
else:
    fac(pwd)






