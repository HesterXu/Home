# -*- coding: utf-8 -*-
# @Time     : 2018/11/9/22:17
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : AutoTraceDraw.py
# @Software : PyCharm

import turtle as t
t.title('自动绘制轨迹')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")   #换行符转为空字符串，去掉换行信息
    datals.append(list(map(eval,line.split(","))))
    # line.split() 用逗号将字符串分隔开，生成一个列表，每个元素就是一个逗号隔开的字符串
    # map() 内嵌函数,将第一个参数的功能作用于第二个函数的每个元素
    # eval评估函数，将列表每个元素两侧的引号去掉
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])






