# -*- coding: utf-8 -*-
# @Time     : 2018/11/5/7:12
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : SevenDigitsDrawV2.py
# @Software : PyCharm


#SevenDigitsDrawV2      七段数码管绘制
import turtle as t
import time

def drawGap():
    t.penup()
    t.fd(5)
def drawLine(draw):        #绘制单段数码管
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
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
    t.pencolor('red')
    for i in date:
        if i == '-':
            t.write("年",font=("Arial",18,"normal"))
            t.pencolor("green")
            t.fd(40)
        elif i == '=':
            t.write("月",font=("Arial",18,"normal"))
            t.pencolor("blue")
            t.fd(40)
        elif i == '+':
            t.write("日", font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))

def main():
    t.setup(950,350,200,200)
    t.penup()
    t.fd(-200)
    t.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    #drawDate('20180905')
    t.hideturtle()
    t.done()
main()
