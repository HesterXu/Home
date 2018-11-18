# -*- coding: utf-8 -*-
# @Time     : 2018/11/17/9:45
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : class_object_02.py
# @Software : PyCharm


class SeniorTestingEngineer:
    #属性
    workyear = 3
    salary = 20000
    #行为  对象方法
    def coding(self,lan):  #这是一个对象方法
        print("会写{0}代码".format(lan))
        print("工作年限是{},月薪是{}".format(self.work_year,self.salary))

    @staticmethod   #静态方法：不需要特意创建对象来调用
    def do_sql(name):
        print("会sql数据库")
    @classmethod   #类方法
    def do_linux(cls):
        print("cls的值是：",cls)
        print("会操作linux")
        print("工作年限是{},月薪是{}".format(cls.work_year, cls.salary))

    def do_function_testing(self):
        print("会做功能测试")

#克隆一个符合规则的个体
#创造一个对象
# p1=SeniorTestingEngineer()
# p2=SeniorTestingEngineer()
# p3=SeniorTestingEngineer()
# #对象拥有类里面的所有属性和函数的使用权，类里面的函数只能由对象调用
# p1.do_api_testing()
# print(p1)
# p2.do_function_testing()
# p3.coding('python')
# print(p3)

# 对象方法  静态方法
# self   @sta
# 对象方法可以通过对象self调用类里面的任意属性值，静态方法无法调用属性值
# 如果一个方法跟类里面的属性没有任何关联，可以用静态方法
# 静态方法和类方法 支持对象调用，也支持类名直接调用

SeniorTestingEngineer.do_sql('mysql')
SeniorTestingEngineer.do_linux()
