# -*- coding: utf-8 -*-
# @Time     : 2018/11/12/20:07
# @Author   : Hester Xu
# Email     : xuruizhu@yeah.net
# @File     : Lesson8_20181112.py
# @Software : PyCharm

import os

# 1. 新建一个目录
#os.mkdir("Python12")
#os.mkdir(r"D:\Project\MOOC\Lemon\Python_Base\Lesson8_20181112\Py12")
#2. 删除一个目录
#os.rmdir("Python12")
# 3. 建立多级目录,不能跨级新建文件，确保除最后一级以外的目录级别都存在
# os.mkdir("py12")
# os.mkdir("py12/A")
# 4. 删除包含有子文件夹的目录，不能跨级删除
#os.rmdir("py12")


#  怎么获取路径的值
# 5.获取当前的工作路径，具体到目录
# path = os.getcwd()
# print(path)
# 6. 获取当前的工作路径，具体到文件
# path_2 = os.path.realpath(_file_)  #表示文件本身
# print(path_2)

#如何获取
#1. 方法一：D:\Project\MOOC\Lemon\Python_Base\Lesson8_20181112\py12\A\b.txt
# 方法二：
# 方法三：getcwd()  OK
# 方法四：realpath  OK
# real_path = os.path.realpath(_file_)
# print()

#判断当前的路径 是目录 or 文件？

# os.path.isdir()
# os.path.isfile()
# os.listdir()
# os.path.dirname()
# os.path.basename()

# os.path.join()
