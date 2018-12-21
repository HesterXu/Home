# -*- coding: utf-8 -*-
# @Time     : 2018/12/7/7:25
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson18_ddt_01_20181205.py
# @Software : PyCharm

# ddt: data drive test 数据驱动测试
# 结合单元测试去执行用例
# 装饰器  装饰函数--拓展

# def print_msg(**kwargs):  # 关键字参数
#     print(kwargs)

def print_msg(*args):  # 动态参数
    print("{},参数的长度是：{}".format(args,len(args)))

print_msg(1,2,3,4,5,'hello')   # 到了函数内部，会变成一个元组。元组里有6个元素
print("---------------------------------")

a = (1,2,3,4,5,'hello')
print_msg(a)    # 元组里有1个元素
print_msg(*a)   # 元组里有6个元素,加了星号,脱外套
print("---------------------------------")

a = [1,2,3,4,5,'hello']
print_msg(a)    # 元组里有1个元素
print_msg(*a)   # 元组里有6个元素,加了星号,脱外套
print("---------------------------------")

a = [[1,2,3,4],[5,'hello']]
print_msg(a)    # 元组里有1个元素
print_msg(*a)   # 元组里有2个元素,加了星号,脱外套,只脱了一层

