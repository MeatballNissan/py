# -*- coding: utf-8 -*-
# @Time    : 2019-03-03 16:39
# @Author  : bxd
# @Email   : 8981540@qq.com
# @File    : test.py
# @Software: PyCharm

#from module import *  #不建议这样用，容易被重载
'''
    模块： 一个python文件，用来组织（变量 函数 类 逻辑）
    包：一个带有__init__.py的文件夹，用于组织模块
    import 模块本质：将文件解释一遍
    import 包本质：执行包下的__init__.py文件
'''

import module #将整个文件形成一个变量   import 本质：将文件解释一遍
from module import name as name3  #只取name形成一个变量
from module import hello
import sys,os
# module.hello()
# print(module.name)

name = 'aaa'

print(module.name)

# print(name3)

name3 = 'bbb'
hello()
print(sys.path)
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
