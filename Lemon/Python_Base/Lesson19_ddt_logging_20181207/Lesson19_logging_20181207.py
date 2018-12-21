# -*- coding: utf-8 -*-
# @Time     : 2018/12/7/21:22
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson19_logging_20181207.py
# @Software : PyCharm

# 日志：记录代码执行的过程，一旦记录下来，就可以根据日志去定位排查问题

# 日志的级别： debug info waring error critical  # 可以自定义日志输出的级别，灵活控制
# 为何不用print

# python自带的logging模块

# root logger   系统自定义的日志的收集器  默认收集并输出warning以及它级别以上的日志信息
# handlers   输出渠道  默认是console 控制台

import logging

# logging.debug('段德斌同学，你这个是一个debug信息')
# logging.info('单单军同学，你这个是一个信息')
# logging.warning('33同学，你这个是一个warningg信息')
# logging.error('David同学，你这个是一个error信息')
# logging.critical('404同学，你这个是一个critical信息')

# 创建自己的日志收集器
qq_logger = logging.getLogger('Hester')  # getLogger()  创建一个日志收集器
qq_logger.setLevel('INFO')   # 设置自己的日志收集器的级别

# 指定输出格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

# 指定自己的输出渠道 - 控制台
ch = logging.StreamHandler()   # 输出到控制台   ch = console handler
ch.setLevel('DEBUG')          # 设置自己的输出渠道的级别
ch.setFormatter(formatter)     # 规定日志输出时，按照指定的formatter格式

# 指定自己的输出渠道 - 本地文件
fh = logging.FileHandler('python12.txt',encoding='utf-8')
fh.setLevel('INFO')
fh.setFormatter(formatter)

# 对接
qq_logger.addHandler(ch)
qq_logger.addHandler(fh)

qq_logger.debug('Anna,这是一个debug信息')
qq_logger.info('Nicky,这是一个info信息')
qq_logger.warning('David,这是一个waring信息')
qq_logger.error('404，这是一个error信息')
qq_logger.critical('路人甲，这是一个critical信息')



