# -*- coding: utf-8 -*-
# @Time     : 2018/12/11/15:57
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : project_path.py
# @Software : PyCharm

# 存储路径的变量
import os

# path = os.path.realpath(__file__)  # 绝对路径，精确到模块名
# print(path)   # D:\Project\MOOC\Lemon\Python_Base\api_auto_4\common\project_path.py

# path = os.path.split(os.path.realpath(__file__)) # os.path.split()，对路径拆分，得到一个元组，有两个元素
# print(path)  # ('D:\\Project\\MOOC\\Lemon\\Python_Base\\api_auto_4\\common', 'project_path.py')

# path = os.path.split(os.path.realpath(__file__))[0] # 取元组的第一个元素
# print(path)  # D:\Project\MOOC\Lemon\Python_Base\api_auto_4\common

# path = os.path.split(os.path.split(os.path.realpath(__file__))[0]) # 再次拆分，得到一个元组，有两个元素
# print(path)  # ('D:\\Project\\MOOC\\Lemon\\Python_Base\\api_auto_4', 'common')

base_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] # 取元组的第一个元素，得到基础路径
# print(base_path)  # D:\Project\MOOC\Lemon\Python_Base\api_auto_4

# 配置文件的路径
config_path = os.path.join(base_path,'configs','test_api.configs')
# 测试报告的路径
report_path = os.path.join(base_path,'test_result','report','test_api.html')
# 日志的路径
log_path = os.path.join(base_path,'test_result','log','test_api_log.txt')
# 测试用例的路径
case_path = os.path.join(base_path,'datas','test_cases.xlsx')

