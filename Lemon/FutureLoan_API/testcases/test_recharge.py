# -*- coding: utf-8 -*-
# @Time     : 2018/12/24/21:02
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @Software : PyCharm
# @File     : test_recharge.py
# @Function : 

import unittest
import json
from Lemon.FutureLoan_API.common.do_excel import DoExcel
from Lemon.FutureLoan_API.common import contants
from Lemon.FutureLoan_API.common.request import Request
from ddt import ddt,data,unpack

do_excel = DoExcel(file_name=contants.case_file)  # 实例化一个DoExcel对象
cases = do_excel.get_cases('login')  # 返回一个case列表，由一个个Case对象/实例

@ddt
class TestRecharge:

    @data
    def test_recharge(self):
        pass
    


