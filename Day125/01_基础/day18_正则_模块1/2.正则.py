# 计算器
# re模块
# 正则表达式 —— 字符串匹配的
# 学习正则表达式
# 学习使用re模块来操作正则表达式
# while True:
#     phone_number = input('please input your phone number ： ')
#     if len(phone_number) == 11 \
#             and phone_number.isdigit()\
#             and (phone_number.startswith('13') \
#             or phone_number.startswith('14') \
#             or phone_number.startswith('15') \
#             or phone_number.startswith('18')):
#         print('是合法的手机号码')
#     else:
#         print('不是合法的手机号码')


# import re
# phone_number = input('please input your phone number ： ')
# if re.match('^(13|14|15|18)[0-9]{9}$',phone_number):
#         print('是合法的手机号码')
# else:
#         print('不是合法的手机号码')


# 绿茶 白茶 黄茶 青茶（乌龙茶） 红茶 黑茶
# 发酵程度和制作工艺
# print(r'\\n')
# print(r'\n')
