# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 11:07
# @Author  : Hester Xu
# @Email   : xuruizhu@yeah.net
# @File    : myclass_homework_20181126.py
# @Software: PyCharm


'''
1：自己写一个工具类，完成数学的加减乘除以及平方积操作。
2：对每个方法写2个用例。
3：针对测试用例选用不同的方法去执行，然后生成测试报告。
下一节课内容：cookie session token key 以及工具的使用！
'''

# 一个工具类，完成数学的加减乘除以及平方积操作。
class MathTool():

    def sum(self,a,b):
        # print("a + b 的值是：",a + b)
        return a + b

    def sub(self,a,b):
        # print("a - b 的值是：",a - b)
        return a - b

    def mul(self,a,b):
        # print("a * b 的值是：",a * b)
        return a * b

    def div(self, a, b):
        # print("a / b 的值是：", a / b)
        return a / b

    def squ(self,a,b):
        # print("a 和 b的平方积的值是：",pow(a,2) * pow(b,2))
        return pow(a,2) * pow(b,2)

