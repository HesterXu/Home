# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/23:00
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : my_log.py
# @Software : PyCharm

"""写一个可配置的日志类"""
import logging
from Lemon.Python_Base.api_auto_4.common.read_config import ReadConfig
from Lemon.Python_Base.api_auto_4.common import project_path

class MyLog:

    def my_log(self,level,msg):
        # 创建一个日志收集器logger并设置其日志级别为DEBUG
        my_logger = logging.getLogger(ReadConfig().read_config(project_path.config_path, 'MY_LOGGER', 'logger_name'))  # 创建自己的日志收集器
        my_logger.setLevel(ReadConfig().read_config(project_path.config_path, 'MY_LOGGER', 'logger_level'))   # 设置自己的日志收集器的级别

        # 指定日志输出格式
        formatter = logging.Formatter(ReadConfig().read_config(project_path.config_path, 'MY_LOGGER', 'log_formatter'))

        # Handler指定自己的输出渠道 - 控制台
        ch = logging.StreamHandler()      # 日志输出到控制台
        ch.setLevel(ReadConfig().read_config(project_path.config_path, 'MY_LOGGER', 'console_handle_level'))  # 设置日志的输出渠道（控制台）的级别
        ch.setFormatter(formatter)        # 日志输出时按照指定的formatter格式

        # Handler指定自己的输出渠道 - 本地文件
        fh = logging.FileHandler(project_path.log_path, encoding='utf-8')  # 日志输出到指定文件
        fh.setLevel(ReadConfig().read_config(project_path.config_path, 'MY_LOGGER', 'file_handle_level'))          #  设置日志的输出渠道（指定文件）的级别
        fh.setFormatter(formatter)         # 日志输出时按照指定的formatter格式

        # 对接
        my_logger.addHandler(ch)  # 日志收集器logger和输出渠道（控制台）对接
        my_logger.addHandler(fh)  # 日志收集器logger和输出渠道（指定文件）对接

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

        # 移除多余的日志
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log('DEBUG',msg)      # 类里面函数间的相互调用 MyLog().my_log('DEBUG',msg)是错误的！！！
    def info(self,msg):
        self.my_log('INFO', msg)
    def warning(self,msg):
        self.my_log('WARNING', msg)
    def error(self,msg):
        self.my_log('ERROR',msg)
    def critical(self,msg):
        self.my_log('CRITICAL', msg)

if __name__ == '__main__':
    my_Logger = MyLog()
    my_Logger.debug("这是个日志信息!")


