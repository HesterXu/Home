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

# 写一个配置类  参数化
import configparser
from Lemon.Python_Base.api_auto_4.common import project_path


class ReadConfig:
    def read_config(self,filename,section,option):
        cf = configparser.RawConfigParser()
        cf.read(filename, encoding='utf-8')
        value = cf.get(section,option)
        return value

# print(ReadConfig().read_config())
if __name__ == '__main__':
    button = ReadConfig().read_config(project_path.config_path,'CASE','button')
    print(button)

