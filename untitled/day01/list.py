from typing import List
import copy
__author__ = "bxd"

names = "a b c d"
namess = ["a","b","c","d"]  # type: List[str]
'''
print(names)
print(namess)
print(namess[2],namess[0])
print(namess[1:3])#切片
print(namess[-1])
print(namess[-2:-1])
print(namess[-2:]) #从倒数第二个 取到最后
print(namess[:2]) #从0开始取到第二个 左闭右开
namess.append("e")
namess.insert(1,"f")
namess[2] = "g"
# 删除方法
namess.remove("d")
del namess[1]
namess.pop()#删除并且返回值，无下标默认删除最后一个

print(namess.index("g"))
print(namess.count("g"))
#namess.clear();
print(namess)
namess.reverse()
print(namess)
namess.sort()#特殊符号  数字 大写 小写 （ascii码）
print(namess)
i = 0
while i<3:
    print("~~")
    print(namess[i])
    i+=1
namess2 = ["2"]
namess.extend(namess2)
print(namess)
del namess2

'''

print(namess)
namess2 = namess.copy()#浅拷贝 ，对象为地址值
print(namess2)
namess.pop()
namess2[1] = "e"
print(namess)
print(namess2)

#copy.copy() 浅拷贝  copy.deepcopy()深拷贝
for i in namess2:
    print(i)

print(range(1,10,2))
print(namess2[0:-1:2])#全部切片，步长2
print(namess2[::2])#全部切片，步长2
print(namess2[:])#全部切片

#浅copy的几种方式
person = ['name',['a',100]]
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)

#元组 只读数组
names2 = ("a", "b", "c", "d")
for i in names2:
    print(i)
