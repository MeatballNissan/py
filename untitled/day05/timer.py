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

import random
print(random.random())
print(random.randint(299,399))
print(random.randrange(21,222))

import os
# os.makedirs("bxd/bxd")
print(os.listdir())
print(os.linesep+"1")

print(os.getcwd())

# os.chdir("/Users/bxd")
print(os.getcwd())

# os.makedirs("/Users/bxd/PycharmProjects/py/untitled/day05/aaa/bbb")
# os.removedirs("/Users/bxd/PycharmProjects/py/untitled/day05/aaa/bbb")

print(os.listdir())

print(os.environ)

# os.stat()
print(os.sep)

print(os.linesep)
print(os.pathsep)

print(os.system('ls -n'))

print(os.path.isabs('/a'))
print(os.path.isabs('bxd'))



import  sys

print(sys.argv)

print(sys.platform)

import  shutil    #拷贝文件 压缩包

f1 = open('a.txt',encoding='utf-8')

f2 = open('b.txt','w',encoding='utf-8')

shutil.copyfileobj(f1,f2)

shutil.copyfile('a.txt','c.txt')


import shelve
import datetime
#shelve 对pickle的上层封装  写为.db文件
d = shelve.open('open_test')
name = ['aaa','bbb','ccc']
d['name'] = name
d['c'] = 'abc'
d['date'] = datetime.datetime.now()


print(d.items())#
print(d.get('name'))
print(d.get('date'))
d.close()



import xml.etree.ElementTree as ET

# import YAML  处理yaml配置文件，需要自己下载库

import configparser as cp
conf = cp.ConfigParser()
conf.read('test.conf')
print(conf['DEFAULT'])
print(conf.sections())
print('DEFAULT' in conf)
print('DEFAULT2' in conf)
print('DEFAULT3' in conf)
print(conf['DEFAULT']['Compression'])

import hashlib

#sha  基于hash   原则上比md5安全
#md5  也是基于hash