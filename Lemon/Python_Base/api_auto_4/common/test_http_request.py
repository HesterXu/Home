# -*- coding: utf-8 -*-
# @Time     : 2018/12/9/15:14
# @Author   : Hester Xu
# @Email     : xuruizhu@yeah.net
# @File     : test_http_request.py
# @Software : PyCharm

import unittest
# import time
from Lemon.Python_Base.api_auto_4.common.http_request import Http_Request
from ddt import ddt,data
from Lemon.Python_Base.api_auto_4.common.read_config import ReadConfig
from Lemon.Python_Base.api_auto_4.common.do_excel import DoExcel
from Lemon.Python_Base.api_auto_4.common.my_log import MyLog
from Lemon.Python_Base.api_auto_4.common import project_path

COOKIES = None
# 利用我们写的配置类，从配置文件test_api.conf读取出 session和option的值
button = ReadConfig().read_config(project_path.config_path,'CASE','button')
# 调用do_excel模块里的DoExcel类里面的get_data方法， 方法需要几个参数：  文件名，表单名，配置值
test_data = DoExcel().get_data(project_path.case_path,'test_data',button)
# 日志类   可以用它来收集日志
my_logger = MyLog()

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self,item):
        global COOKIES
        my_logger.info("目前正在执行第{}条用例：{}".format(item['case_id'],item['title']))
        my_logger.info("-----------------------开始检查URL地址--------------------------")
        my_logger.info('url:{}'.format(item['url']))

        my_logger.info("-----------------------开始检查param参数--------------------------")
        my_logger.info('param:{}'.format(item['param']))

        my_logger.info("-----------------------开始http请求--------------------------")
        res = Http_Request().http_request(item['url'],eval(item['param']),item['http_method'],COOKIES)
        # excel中的param是str，实际是字典
        my_logger.info("-----------------------结束http请求--------------------------")

        my_logger.info("请求结果是：{}".format(res.json()))
        if res.cookies:
            COOKIES = res.cookies

        my_logger.info("-----------------------开始断言--------------------------")
        try:
            self.assertEqual(str(item['expected']),res.json()['code'])  # excel中的期望值是int，实际是str
            # TestResult = 'PASS'
        except AssertionError as e:
            # TestResult = 'FAIL'
            my_logger.error("断言出错了: {}".format(e))
            raise e
        finally:
            # my_logger.info("本条用例的测试结论是：{}".format(TestResult))
            my_logger.info("-----------------------结束断言--------------------------")
            # time.sleep(1)

