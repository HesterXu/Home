# -*- coding: utf-8 -*-
# @Time     : 2018/11/7/22:13
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson6_function_homework_20181107.py
# @Software : PyCharm

'''
2：写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5 6、写函数，检查传入列表的长度，
如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
如果字符串不在字典中，则添加到字典中，并返回新的字典。
'''

<<<<<<< HEAD
=======
def Reviewlen(s):
    if int(len(s)) > 2:
        s_new = s[0:2]
    #elif s is list and len(s)
    return s_new

s = input("请输入一个对象(字符串，列表，元组)：")
print(Reviewlen(s))




















>>>>>>> origin/master
'''
1：一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。
编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
<<<<<<< HEAD
'''
'''
=======

>>>>>>> origin/master
def joinTeam(g,x,y,k):
    sum = 0
    for i in range(k):
        gender = input("请输入你的性别(男：m，女：f)：")
        age = eval(input("请输入你的年龄(正整数)："))
        if gender == g and x <= age <= y:
            print("恭喜你，可以加入球队！")
            sum += 1
        else:
            print("很遗憾，你不可以加入球队!")
<<<<<<< HEAD
    #return print("一共有{}人可以加入球队".format(sum))
    print("一共有{}人可以加入球队".format(sum))

joinTeam('m',10,20,3)
'''
'''
def judge(a):
    if len(a) > 5:
        print(True)
    else:
        print(False)

judge([1,2,3,4,5,6])
'''
'''
def check_list(L):
     if len(L) > 2:
         del L[2:]   #切片以及del函数
     else:
         pass
     return L
r = check_list([1,2,3])
print(r)
'''
def judge_dict(d,s):
    if s not in d.values():
        if s not in d.keys():
            d[s] = s
        else:
            d[s+"_1"] = s
    return d
r = judge_dict({"name":"rui"},"name")
print(r)




=======
    return print("一共有{}人可以加入球队".format(sum))
joinTeam('m',10,20,3)
'''
>>>>>>> origin/master









