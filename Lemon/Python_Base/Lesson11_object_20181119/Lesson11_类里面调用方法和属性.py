# -*- coding: utf-8 -*-
# @Time     : 2018/11/20/20:31
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson11_类里面调用方法和属性.py
# @Software : PyCharm

'''
类里面 调用方法和属性：
# 1.对象方法里：对象调用属性，类名调用属性 self.name  RobotOne.name
# 2.类方法里：  类名调用属性              cls.name   RobotOne.name
# 3.静态方法里：类名调用属性                         RobotOne.name
'''

class RobotOne:
    birthday = '20181119'
    name = 'hester'

    def talk(self):     # 创建对象后，self就是对象本身，self才有意义。
        print(self)     # <__main__.RobotOne object at 0x00000000021E60B8>
        print(self.name + "可以跟你进行简单交流")        # 对象调用属性
        print(RobotOne.name + "可以跟你进行简单交流")    # 类名调用属性
        # self.walk()     # 调用walk（） 对象调用类方法
        # self.sing()     # 调用sing（） 对象调用静态方法
        # RobotOne.walk()   # 调用walk（） 类名调用类方法
        # RobotOne.sing()   # 调用sing（） 类名调用静态方法

    @classmethod
    def walk(cls):  # cls就是类本身RobotOne
        print(cls)      # <class '__main__.RobotOne'>
        print(cls.name+"会直线行走")            # 类名调用属性
        print(RobotOne.name + "会直线行走")     # 类名调用属性
        # cls.sing()    # 调用sing（） 类名调用静态方法
        # RobotOne.sing() # 调用sing（） 类名调用静态方法


    @staticmethod
    def sing():   # 静态方法，当方法里面不需要用到类的属性值时，可以写成静态方法。
        print("会播放音乐")      # 静态方法里一般不会用到类属性；如果要用到类属性，可以写成对象方法
        print(RobotOne.name)     # 类名调用属性

r1 = RobotOne()
r1.talk()
print('===========1============')
r1.walk()
print("===========2==========")
r1.sing()




class RobotOne:
    def __init__(self, birthday, name,*args,**kwargs):   # 初始化函数，创建对象的时候去传值，没有return
        # 属性只有类和对象可以调用，所以可以把属性传给类或者对象
        #RobotOne.birthday = birthday   # 把属性传给类，类里面的属性对象都可以调用，所以此时类和对象都可以调用属性
        #RobotOne.name = name
        self.birthday = birthday        # 把属性传给对象，只有对象可以调用，类不可以调用属性
        self.name = name
        self.hobby = args       # 动态参数 -- 元组
        self.kwargs = kwargs    # 关键字参数  -- 字典

    def talk(self,content):
        print(self.name + "可以跟你进行简单交流" + content)  # 对象调用属性
        #print(RobotOne.name + "可以跟你进行简单交流")  # 把属性传给对象，只有对象可以调用，类不可以调用
        #  AttributeError: type object 'RobotOne' has no attribute 'name'
        print(self.name,"业余爱好是：",self.hobby)   # 动态参数 -- 在函数里 -- 元组
        print(self.name,'业余爱好是：',self.kwargs)  # 关键字参数 -- 在函数里 -- 字典

    @classmethod
    def walk(cls,des1,des2):  # cls就是类本身RobotOne
        print("会直线行走" + des1 + des2)
        # print(cls.name + "会直线行走")  # 类名调用属性 # AttributeError: type object 'RobotOne' has no attribute 'name'
        # print(RobotOne.name + "会直线行走")  # 类名调用属性

    @staticmethod
    def sing(music):  # 静态方法，当方法里面不需要用到类的属性值时，可以写成静态方法。
        print("会播放音乐" + music)  # 静态方法里一般不会用到类属性；如果要用到类属性，可以写成对象方法
        # print(RobotOne.name)  # 类名调用属性  # AttributeError: type object 'RobotOne' has no attribute 'name'

r2 = RobotOne('20181111','许蕊竹','football','basketball','swimming',a = '111',b='666')
r2.talk('好好学习，天天向上！！！')
r2.walk('从深圳出发','一直走到新西兰')
r2.sing('隐形的翅膀')


