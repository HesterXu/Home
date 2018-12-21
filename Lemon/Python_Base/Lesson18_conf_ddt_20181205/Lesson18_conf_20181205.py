# -*- coding: utf-8 -*-
# @Time     : 2018/12/5/19:52
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson18_conf_20181205.py
# @Software : PyCharm

"""配置文件的相关知识"""
# ini. properties. configs 等等 都是配置文件
# 存在配置文件里的数据，读取出来后，全都是字符串类型
# section 片段，用法：[片段名]  "[section]" header
# option 选项  "name: value" entries

# 1.怎么读取数据？
import configparser
"""A configuration file consists of sections, lead by a "[section]" header,
and followed by "name: value" entries, with continuations and such in
the style of RFC 822.
Intrinsic defaults can be specified by passing them into the
ConfigParser constructor as a dictionary."""

cf = configparser.ConfigParser()   # 创建对象  可以读取配置文件信息的对象

"""导入第三方库 configparser
创建ConfigParser类的对象 cf
ConfigParser类继承了RawConfigParser类
对象cf调用RawConfigParser类的函数"""

"""RawConfigParser类下面有read(),sections(),options()等函数"""

cf.read('case.configs',encoding='utf-8')  # 类似open函数
print(cf.sections())
print(cf.options('Student'))

# section和option组合  可以帮我们确定一个想要的值
print(cf.get('Student','name'),type(cf.get('Student','name')))
print(cf.get('Student','age'),type(cf.get('Student','age')))
print(cf.get('Student','height'),type(cf.get('Student','height')))
print(cf.get('Student','score'),type(cf.get('Student','score')))

# 两种读取数据的方式：
print(cf.get('Student','height'))
print(cf['Student']['height'])

# 写成一个配置类  参数化
class ReadConfig:
    def read_config(self,filename,section,option):
        cf = configparser.RawConfigParser()
        cf.read(filename, encoding='utf-8')
        value = cf.get(section,option)
        return value

# print(ReadConfig().read_config())
if __name__ == '__main__':
    value = ReadConfig().read_config('case.configs','Student','score')
    print(value)
