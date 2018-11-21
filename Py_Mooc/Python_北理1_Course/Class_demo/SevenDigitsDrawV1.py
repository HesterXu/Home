# -*- coding: utf-8 -*-
# @Time     : 2018/11/5/6:36
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : SevenDigitsDrawV1.py
# @Software : PyCharm

#SevenDigitsDrawV1   七段数码管绘制
import turtle as t

def drawLine(draw):        #绘制单段数码管
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)
def drawDigit(digit):     #根据数字绘制7段数码管
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 4, 6, 7, 8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 7, 8, 9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawDate(date):
    for i in date:
        drawDigit(eval(i))
def main():
    t.setup(200,200,850,300)
    t.penup()
    t.fd(-200)
    t.pensize(5)
    drawDate('20180905')
    t.hideturtle()
    t.done()
main()



