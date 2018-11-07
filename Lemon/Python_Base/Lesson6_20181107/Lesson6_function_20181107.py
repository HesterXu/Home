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
# return：可以有0个或多个返回值，多个值返回的是元组
# 可以有return，也可以没有
# return 后没有变量， 或者没有return，返回的都是None
# 当要利用函数的返回值做其他操作时，要return结果出来。
# 怎么写一个函数：
# 1. 先用代码写出功能，甚至可以用一组数据替代进去 写代码
# 2. def 函数名 变成函数
# 3. 思考怎么提高复用性

# 动态参数： *变量名    *args   arguments
# 动态参数：不定长参数=不定个数  不定长参数：元组

# 关键字参数  **kwargs   key word arguments   变成了字典
# 关键字参数   可以接收任意多个参数

# 参数的混合使用， 要注意顺序：
# 位置参数，动态参数，默认值参数，关键字参数


'''
s = [1,3,4]
s.pop()  #
print(s)

a = 'hello'
new_a = a.replace('h','@')  #
print(a)
print(new_a)
'''




'''
def sum(a,b):
    s = 0
    for i in range(a,b):
        s += i
    #print("{}到{}的和是{}".format(a,b-1,s))
    return s
print(sum(1,101))
'''










