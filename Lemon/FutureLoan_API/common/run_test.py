# -*- coding: utf-8 -*-
# @Time     : 2018/12/21/15:58
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @Software : PyCharm
# @File     : run_test.py
# @Function : 

"""20181219作业：
1，设计一个run_test 模块完成收集用例--执行用例--回写测试结果
2，封装配置文件读取类，根据环境设计配置文件，实现多套环境灵活切换
3，复习unittest,ddt
"""
import json
from Lemon.FutureLoan_API.common.do_excel import DoExcel
from Lemon.FutureLoan_API.common.request import Request

# 测试DoExcel类
do_excel = DoExcel(file_name='../datas/cases.xlsx')  # 实例化一个DoExcel对象
sheet_names = do_excel.get_sheet_names()                    # 获取到workbook里面所有的sheet名称的列表
print("sheet名称列表：", sheet_names)
case_list = ['login']               # 定义一个执行测试用例的列表
for sheet_name in sheet_names:
    if sheet_name in case_list:   # 当前的sheet_name不在可执行的case_list里面，就不执行
        cases = do_excel.get_cases(sheet_name)   # 测试用例列表,由一个个Case对象/实例组成
        print(sheet_name+"测试用例个数：",len(cases))
        for case in cases:              # 遍历测试用例列表
            print("case信息：",case.__dict__)  # 打印case信息
            data = eval(case.data)    # 从excel中取到的data是一个字符串，把字符串转为字典
            resp = Request(method=case.method,url=case.url,data=data)
            print("status_code：",resp.get_status_code())  # 打印响应码
            resp_dict = resp.get_json()  # 获取请求响应，字典
            print("resp_dict ：",resp_dict)
            resp_text = json.dumps(resp_dict,ensure_ascii=False,indent=4) # 将字典转化为字符串
            print("response：",resp_text)  # 打印响应
            # 判断接口响应和excel里面expected的值是否一致
            if case.expected == resp.get_text():
                print("result: PASS")
                # 期望结果与实际结果一致，就写入PASS到result这个单元格
                do_excel.write_back_by_case_id(sheet_name=sheet_name,case_id=case.case_id,actual=resp.get_text(),result='PASS')
            else:
                print("result: FAIL")
                # 期望结果与实际结果不一致，就写入FAIL到result这个单元格
                do_excel.write_back_by_case_id(sheet_name=sheet_name,case_id=case.case_id,actual=resp.get_text(),result='FAIL')



