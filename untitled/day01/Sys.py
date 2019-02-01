__author__ = "bxd"
import sys
import os
import Test

# print(sys.path) #打印python环境变量
a = """
['/home/bxd/PycharmProjects/untitled',
 '/home/bxd/PycharmProjects/untitled',
 '/usr/lib/python35.zip',
 '/usr/lib/python3.5',
 '/usr/lib/python3.5/plat-x86_64-linux-gnu',
 '/usr/lib/python3.5/lib-dynload',
 '/home/bxd/PycharmProjects/untitled/venv/lib/python3.5/site-packages',
 '/home/bxd/PycharmProjects/untitled/venv/lib/python3.5/site-packages/setuptools-39.1.0-py3.5.egg',
 '/home/bxd/PycharmProjects/untitled/venv/lib/python3.5/site-packages/pip-10.0.1-py3.5.egg',
 '/usr/local/pycharm/pycharm-2018.3.2/helpers/pycharm_matplotlib_backend']
"""
print(sys.argv)
# print(sys.argv[2])
print(os.path)
ab = os.system("ls -n")#只执行命令 不保存结果
print(ab)# 0代表执行成功

cd = os.popen("ls -n")
print(cd) #打印地址值
cd = os.popen("ls -n").read()
print(cd) #打印出结果
# 1.当前路径 2.环境变量找模块