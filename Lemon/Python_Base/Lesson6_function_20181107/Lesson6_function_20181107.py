# -*- coding: utf-8 -*-
# @Time     : 2018/11/7/20:04
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson6_function_20181107.py
# @Software : PyCharm

# 函数：
# append pop insert range print input int str list replace strip split
# 内置函数
# 参数：可以是0个，1个，或多个。 有参数时，调用时必须传参。

# return 变量的个数    变量个数可以是0个或多个  多个变量用逗号隔开  多个变量返回的是元组
# 可以有return，也可以没有
# return 后没有变量， 或者没有return，返回的都是None
# return作用：当你调用函数的时候，返回一个结果给函数，函数终止
# 当要利用函数的返回值做其他操作时，要return结果出来。

# 怎么写一个函数：
# 1. 先用代码写出功能，甚至可以用一组数据替代进去 写代码
# 2. def 函数名   变成函数
# 3. 思考怎么提高复用性

# 参数：默认按顺序赋值 不想按顺序赋值，可以按名称赋值，但是名称要跟参数名保持一致

# 位置参数
# 默认值参数/名称参数：定义一个默认值

# 动态参数：也叫不定长参数, 不定个数       不定长参数变成了：元组
# 动态参数： *变量名    *args   arguments
# 动态参数：  可以接收任意多个参数

# 关键字参数  **kwargs   key word arguments   关键字参数变成了：字典
# 关键字参数   可以接收任意多个参数/键值对

# 参数的混合使用,要注意顺序：
# 一般规则：位置参数，动态参数，默认值参数，关键字参数！！！
# 默认值参数必须放在位置参数后面
# 位置参数，动态参数，默认值参数的顺序：要想取默认值，默认值参数放在最后......





'''
# 按顺序赋值，1给a，2给b，其他的给args
def print_msg(a,b=10,*args):
    print("a:",a)
    print("b:",b)
    print("args:",args)
print_msg(1,2,3,4,5,6)    # a=1,b=2,args=(3,4,5)
'''

'''
# 默认值参数必须放在位置参数后面, b=10放在a前面是错误的！！！
def print_msg(b=10,a,*args):
    print("a:",a)
    print("b:",b)
    print("args:",args)
print_msg(1,2,3,4,5,6)
'''

'''
# 要想让b=10不变，把b=10放在最后。1给了a，其他的全给了args。
def print_msg(a,*args,b=10):
    print("a:",a)
    print("b:",b)
    print("args:",args)
print_msg(1,2,3,4,5,6)  # a=1,b=10,args=(2,3,4,5,6)
'''

'''
# 这种情况下：args不能放在a前面，全部传给了args，a没有了值。
def print_msg(*args,a,b=10):
    print("a:",a)
    print("b:",b)
    print("args:",args)
print_msg(1,2,3,4,5) 
'''
'''
def print_msg(*args,a,b=10):
    print("a:",a)
    print("b:",b)
    print("args:",args)
print_msg(2,3,4,5,6,a=1)  # a=1放在最后是可以的，不能放在最前面
'''







'''
# 内置函数 pop()   replace()
s = [1,3,4]
s.pop()  # 会删除最后一个元素，然后返回这个被删除的值
print(s)        # [1,3]
print(s.pop())  # 4

a = 'hello'
new_a = a.replace('h','@')  # 会返回一个新的字符串，原来的字符串不变
print(a)      # hello
print(new_a)  # @ello
'''
'''
# 怎么提高函数的复用性
def sum(a,b):
    s = 0
    for i in range(a,b):
        s += i
    #print("{}到{}的和是{}".format(a,b-1,s))
    return s
print(sum(1,101))
'''










