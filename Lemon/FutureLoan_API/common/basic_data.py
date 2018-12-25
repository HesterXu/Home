# -*- coding: utf-8 -*-
# @Time     : 2018/12/24/20:39
# @Author   : Hester Xu
# @Email    : 1603046502@qq.com
# @Software : PyCharm
# @File     : basic_data.py
# @Function : 测试上下文


class Context:   # 初始化函数里面的变量是成员变量

    normal_user = 123   # 类里面的变量是类变量
    pwd = None



if __name__ == '__main__':
    # python的反射 动态获取对象里面的
    normal_user = getattr(Context,'normal_user')  # 获取变量的值
    print(normal_user)
    setattr(Context,'admin_user','abc')
    admin = getattr(Context,'admin_user')
    print(admin)
    if hasattr(Context,'admin_user'):
        delattr(Context,'admin_user')
    else:
        print("没有这个属性，不删除")




# 变量一样时，成员变量覆盖类变量
# 不需要实例可以调用