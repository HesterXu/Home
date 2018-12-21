# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/16:32
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : config.py
# @Software : PyCharm

"""配置文件的相关知识"""
# ini. properties. configs 等等 都是配置文件
# 存在配置文件里的数据，读取出来后，全都是字符串类型
# section 片段，用法：[片段名]  "[section]" header
# option 选项  "name: value" entries

import configparser

'''
# 1.怎么读取数据？
cf = configparser.ConfigParser()   # 创建对象  可以读取配置文件信息的对象
cf.read('case.configs',encoding='utf-8')  # 类似open函数
print(cf.sections())
print(cf.options('Student'))

# section和option组合  可以帮我们确定一个想要的值
print(cf.get('Student','name'),type(cf.get('Student','name')))
print(cf.get('Student','age'),type(cf.get('Student','age')))
print(cf.get('Student','height'),type(cf.get('Student','height')))
print(cf.get('Teacher','hobby'),type(cf.get('Teacher','hobby')))

# 两种读取数据的方式：
print(cf.get('Student','height'))
print(cf['Student']['height'])
'''

# 写成一个配置类  参数化
class ReadConfig:
    def read_config(self,filename,section,option):
        cf = configparser.RawConfigParser()
        cf.read(filename, encoding='utf-8')
        button = cf.get(section,option)
        return button

# print(ReadConfig().read_config())
if __name__ == '__main__':
    button = ReadConfig().read_config('case.configs','CASE','button')
    print(button)

