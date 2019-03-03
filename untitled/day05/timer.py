# -*- coding: utf-8 -*-
# @Time    : 2019-03-03 18:35
# @Author  : bxd
# @Email   : 8981540@qq.com
# @File    : timer.py
# @Software: PyCharm

import time
print(time.process_time())

print(time.altzone)
print(time.asctime())
print(time.localtime())
date = time.localtime()
print( date.tm_yday)
string_2_struct = time.strptime('2022/02/02','%Y/%m/%d')
print(type(string_2_struct))
print(string_2_struct)
print(string_2_struct.tm_year)