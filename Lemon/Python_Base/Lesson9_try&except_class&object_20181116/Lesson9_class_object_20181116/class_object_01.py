# -*- coding: utf-8 -*-
# @Time     : 2018/11/16/21:19
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : class_object_01.py
# @Software : PyCharm

class SeniorTestingEngineer:
    #属性
    workyear = 3
    salary = 20000
    #行为
    def coding(self,lan):  #这是一个对象方法
        print("会写{0}代码".format(lan))
        print(self)
    def do_sql(self):
        print("会sql数据库")
    def do_linux(self):
        print("会操作linux")
    def do_function_testing(self):
        print("会做功能测试")
    def do_api_testing(self):
        print("会做接口测试")
    def do_auto_testing(self):
        print("会做自动化测试")
#克隆一个符合规则的个体
#创造一个对象
p1=SeniorTestingEngineer()
p2=SeniorTestingEngineer()
p3=SeniorTestingEngineer()
#对象拥有类里面的所有属性和函数的使用权，类里面的函数只能由对象调用
p1.do_api_testing()
print(p1)
p2.do_function_testing()
p3.coding('python')
print(p3)
