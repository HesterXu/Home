# -*- coding: utf-8 -*-
# @Time     : 2018/11/17/13:35
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : homework_04.py
# @Software : PyCharm
'''
4：按照以下要求定义一个游乐园门票类，并创建实例调用函数，
完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定）
1)平日票价100元
2)周末票价为平日票价120%
3)儿童半价
'''

class Ticket:
    def __init__(self,time,adult_number,child_number):
        self.time = time
        self.adult_number = adult_number
        self.child_number = child_number
    def get_price(self):
        if self.time == "weekend":
            adult_price = 120
            child_price = 60
        else:
            adult_price = 100
            child_price = 50
        totla_price = adult_price * self.adult_number + child_price * self.child_number
        print("{}个成人和{}个儿童的票价一共是：{}元".format(self.adult_number,self.child_number,totla_price))

time = input("请输入去公园的时间(weekend or weekday)：")
adult_number = eval(input("请输入去公园的成人数量："))
child_number = eval(input("请输入去公园的儿童数量："))

p = Ticket(time,adult_number,child_number)
p.get_price()




