# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/23:00
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : my_log.py
# @Software : PyCharm

"""结合1207上课讲的日志知识，以及配置文件知识点 编写一个属于自己的可控制的日志类，要求如下：
1）日志输出的渠道 可以通过配置文件 指定输出到指定文件或者是指定渠道
2）通过配置文件 可以指定输出日志的格式 formatter
3）通过配置文件 可以指定我们日志收集器收集日志的级别 以及 输出渠道输出日志的级别
4）把这个日志类 结合我们test_http_requst这个测试类来做
 print的信息用 info级别日志信息来代替
异常信息用error级别的日志信息来代替"""

import logging
from Lemon.Python_Base.api_auto_3.read_config import ReadConfig

class MyLog:
    # file_name = ReadConfig().read_config('logging.configs', 'LOG', 'file_name')
    # logger_name = ReadConfig().read_config('logging.configs', 'LOG', 'logger_name')
    # logger_level = ReadConfig().read_config('logging.configs', 'LOG', 'logger_level')  # 指定收集器收集日志的级别
    # output_level = ReadConfig().read_config('logging.configs', 'LOG', 'output_level')  # 指定输出渠道输出日志的级别
    # log_formatter = ReadConfig().read_config('logging.configs', 'LOG', 'formatter')  # 指定输出日志的格式
    # handler = ReadConfig().read_config('logging.configs', 'LOG', 'handler')  # 指定输出到指定文件或者指定渠道

    def my_log(self,level,msg):
        # 创建一个日志收集器logger并设置其日志级别为DEBUG
        my_logger = logging.getLogger(ReadConfig().read_config('logging.configs', 'LOG', 'logger_name'))  # 创建自己的日志收集器
        my_logger.setLevel(ReadConfig().read_config('logging.configs', 'LOG', 'logger_level'))          # 设置自己的日志收集器的级别

        # 指定日志输出格式
        formatter = logging.Formatter(ReadConfig().read_config('logging.configs', 'LOG', 'formatter'))

        # Handler指定自己的输出渠道 - 控制台
        ch = logging.StreamHandler()      # 日志输出到控制台
        ch.setLevel(ReadConfig().read_config('logging.configs', 'LOG', 'output_level'))         # 设置日志的输出渠道（控制台）的级别
        ch.setFormatter(formatter)        # 日志输出时按照指定的formatter格式
        my_logger.addHandler(ch)             # 日志收集器logger和输出渠道（控制台）对接

        # Handler指定自己的输出渠道 - 本地文件
        fh = logging.FileHandler(ReadConfig().read_config('logging.configs', 'LOG', 'file_name'), encoding='utf-8')  # 日志输出到指定文件
        fh.setLevel(ReadConfig().read_config('logging.configs', 'LOG', 'output_level'))          #  设置日志的输出渠道（指定文件）的级别
        fh.setFormatter(formatter)         # 日志输出时按照指定的formatter格式
        my_logger.addHandler(fh)              # 日志收集器logger和输出渠道（指定文件）对接

        # 日志输出
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

    def debug(self,msg):
        self.my_log('DEBUG',msg)
    def info(self,msg):
        self.my_log('INFO',msg)
    def warning(self,msg):
        self.my_log('WARNING',msg)
    def error(self,msg):
        self.my_log('ERROR',msg)
    def critical(self,msg):
        self.my_log('CRITICAL',msg)

if __name__ == '__main__':
    my_logger = MyLog()
    my_logger.debug('日志信息哈哈哈哈')


