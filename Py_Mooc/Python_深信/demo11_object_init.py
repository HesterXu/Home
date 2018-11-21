# -*- coding: utf-8 -*-
# @Time     : 2018/11/21/6:44
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : demo11_object_init.py
# @Software : PyCharm

# 案例，我的日期类MyDate
class MyDate:

    def __init__(self,y,m,d):
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y < 0 or m < 1 or m >12:
            raise Exception("Invalid Date")
        if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
            months[2] = 29
        if d < 1 or d > months[m]:
            raise Exception("Invalid Date")
        self.year = y
        self.month = m
        self.date = d
    def show(self):
        print("%04d-%02d-%02d" %(self.year,self.month,self.date))
try:
    d = MyDate(2018,11,11)
    d.show()
except Exception as e:
    print(e)



