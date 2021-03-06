# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/16:32
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : config.py
# @Software : PyCharm

"""结合1207上课讲的日志知识，以及配置文件知识点 编写一个属于自己的可控制的日志类，要求如下：
1）日志输出的渠道 可以通过配置文件 指定输出到指定文件或者是指定渠道
2）通过配置文件 可以指定输出日志的格式 formatter
3）通过配置文件 可以指定我们日志收集器收集日志的级别 以及 输出渠道输出日志的级别
4）把这个日志类 结合我们test_http_requst这个测试类来做
 print的信息用 info级别日志信息来代替
异常信息用error级别的日志信息来代替"""
import configparser

# 写一个配置类
class ReadConfig:
    def read_config(self,filename,section,option):
        cf = configparser.RawConfigParser()
        cf.read(filename, encoding='utf-8')
        value = cf.get(section,option)
        return value

if __name__ == '__main__':
    button = ReadConfig().read_config('case.configs','CASE','button')
    print(button)
