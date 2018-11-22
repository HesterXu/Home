# -*- coding: utf-8 -*-
# @Time     : 2018/11/22/22:28
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : 1117作业_4_游乐园门票类.py
# @Software : PyCharm
'''
4：按照以下要求定义一个游乐园门票类，并创建实例调用函数，
完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定）
1)平日票价100元
2)周末票价为平日票价120%
3)儿童半价
'''
class Ticket:
    def get_price(self,adult_num,child_num,adult_price = 100):
        s = "零一二三四五六日"
        d = int(input("请输入去游乐园的时间(1到7分别代表星期一到星期日)，用数字表示："))
        while d not in (1,2,3,4,5,6,7):
            d = int(input("输入错误！请重新输入去游乐园的时间数字："))
        if d in (1,2,3,4,5):
            total_price = adult_price * adult_num + adult_price * 0.5 * adult_num
        if d == 6 or d == 7:
            total_price = adult_price * 1.2 * adult_num + adult_price * 0.6 * adult_num
        print("{}个大人和{}个小孩，星期{}去游乐园的总票价是{}元".format(adult_num,child_num,s[d],total_price))

a = Ticket()
a.get_price(1,1,1)




















