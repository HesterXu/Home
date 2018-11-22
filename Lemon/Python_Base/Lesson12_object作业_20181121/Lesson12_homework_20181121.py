# -*- coding: utf-8 -*-
# @Time     : 2018/11/21/22:02
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson12_homework_20181121.py
# @Software : PyCharm


'''
编写一个函数实现大写转小写，小写变大写，并且转换为镜像字符串，并且将字符串变为镜像字符串。
例如：’A’变为’Z’,’b’变为’y
示范字符串： ”sdSdsfdAdsdsdfsfdsdASDSDFDSFa”字符串大写变小写 小写变大写。
'''

def UptoLow(a):
    print(a.upper())

def LowtoUp(b):
    print(b.lower())

def main():
    s = input("请输入字符串：")

    c = input("请选择转换方式(1:大写转换小写, 2:小写转换大写)：")
    if c == '1':
        LowtoUp(s)
    elif c == '2':
        UptoLow(s)
    else:
        input("转换方式输入错误，请重新输入(1:大写转换小写, 2:小写转换大写)：")
main()
