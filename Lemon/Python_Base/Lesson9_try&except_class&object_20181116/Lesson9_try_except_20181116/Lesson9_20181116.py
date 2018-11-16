# -*- coding: utf-8 -*-
# @Time     : 2018/11/16/20:07
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson9_20181116.py
# @Software : PyCharm

#
# s = '柠檬班12期'
# print(s.encode('gbk'))

# L = [33,2,55,99,10]
# #比较n-1轮，
# for i in range(0,len(L)-1):
#     for j in range(0,len(L)-1-i):
#         if L[j] > L[j+1]:
#             L[j],L[j+1] = L[j+1],L[j]
# print(L)

# 文件关闭； 上下文管理器
# with open('python12.txt','w+') as file:
#     print(file.closed)
# print(file.closed)
with open('python12.txt','w+',encoding='utf-8') as file:
    s = ['123\n','哈哈哈\n']
    file.writelines(s)
