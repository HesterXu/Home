# -*- coding: utf-8 -*-
# @Time     : 2018/11/23/20:10
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : unit_test_01.py
# @Software : PyCharm

# 对象调用：对象方法，类方法，静态方法，属性
# 类名调用：类方法，静态方法，属性

# （一）单元测试：
# 1.单元测试：unittest - 接口,python自带 ; pytest - web, 第三方
# 2.单元测试谁做的？ -- 开发
# 3.单元测试是干嘛的？ -- 对单个模块进行的测试，知道没有问题
# 4.为什么要学单元测试？ -- （1）测试自己的代码；（2）利用单元测试完成功能模块的测试 -- 数据驱动测试
# 5.测试的时候一般怎么测试？ -- 测试内容是：“类”
# 6.测试手段：调用里面的方法
# 7.调用方法：数据驱动测试 -- 不同场景需要不同的数据 -- 测试用例 -- 完成这个模块的测试

# （二）unittest
# 1.unittest  python自带
# 2.位置：D:\Program Files (x86)\Python34\Lib\unittest
# 3.必须记住：case  loader  runner  suite
# 4.unittest四大类：
# (1).TestCase：写测试用例  创建一个TestCase类的实例对象
# (2).TestLoader：加载测试用例
# (3).TestSuite：测试集 容器 存放用例
# (4).TextTestRunner：执行用例

# 5.步骤：
# (1).导入unittest库 -- import unittest
# (2).定义一个自己的测试类，并且继承unittest.TestCase类 -- class TestNicky(unittest.TestCase):
# (3).写用例 -- (1).用例是一个个的对象方法 (2).方法名必须以test开头 (3).用例里面除了self不能传递参数
# (4).
# (5).


# 5.TestCase类：unittest库里面的TestCase类 -- unittest.TestCase  -- 查看类的初始化函数，自带的N个方法
class TestCase(object):
    """A class whose instances are single test cases.
    By default, the test code itself should be placed in a method named'runTest'.
    """
def __init__(self, methodName='runTest'):
    """Create an instance of the class that will use the named test
       method when executed. Raises a ValueError if the instance does
       not have a method with the specified name.
    """
# 6.写用例： 先继承TestCase类
# (1).用例是一个个的对象方法 (2).方法名必须以test开头 (3).用例里面除了self不能传递参数

























