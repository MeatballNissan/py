

#可迭代对象  一、集合数据类型： list typle dict set str   二、generator： 生成器和带yield的generator function
#通过 isinstance（）判断是否为可迭代对象  instanceof
from collections import  Iterable
from collections import Iterator

print(isinstance((),Iterable))

#迭代器  ：  可以被next() 调用的并返回下一个值的对象成为迭代器 ： Iterator

print(dir({}))
print(isinstance((i for i in range(10)),Iterator))
print(isinstance((i for i in range(10)),Iterable))
print(isinstance(['a'],Iterator))
print(isinstance(iter(['a']),Iterator))

#iterator为数据流，迭代器计算是惰性的
f = open('bxd.txt','r',encoding='utf-8')
# print(f.readlines());
for line in f: #实现为迭代器
    print(line)


