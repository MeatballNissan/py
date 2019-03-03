from collections import Iterable
from collections import Iterator
import functools
print(abs(-1))
#all 全部为true 则返回true    空返回true
print(all([1,-1]))
print(all([1,-1,False]))
print(all([]))

#any 有一个为True，则返回True， 空返回false
print("================")
print(any([]))
print(any([True,False]))

# ascii 转为字符串
print("================")
print(ascii('中'))
print('2',[ascii(['a','c',11])])

print(bin(-11))

print(bool([]))

#bytearray 字符串改为可修改的字节数组

a = bytes("abcde",encoding= "utf-8")
print(a)
print(a.capitalize(),a)

b = bytearray("abcde",encoding= "utf-8")
print(b[0])
b[0] = 98
print(b.capitalize())
print(b)


#callable
print("\r\n========== callable")
print(callable([]))
def aa():
    return
print(callable(aa))

print("\r\n========== chr ord")
print(chr(33))
print(ord('!'))
print(ord("!"))


print("\r\n========== compile")
# compile()
code = "for i in range(10):print(i)"
c = compile(code,'','exec')
print(c)
exec(c)
exec(code)   #eval可以直接执行表达式， exec可以实现动态导入

# classmethod()


print("\r\n========== dir")
#查看有什么方法
print("\r\n========== divmod")#返回商和余
print(divmod(4,3))
print(divmod(3,3))
print(divmod(0,3))

print("\r\n========== filter")
def sayhi(n):
    print(n)
sayhi(2)

#匿名函数
a = lambda n:print(n)   # n -> syso(n)
a(43)
b = lambda n: print(((n *i for i in range(n))))
b(11)

c = filter(lambda  n: n>5,range(10))
print(c)
print(isinstance(c,Iterator))
for i in c:
    print(i)

print("\r\n========== map")
d = map(lambda n:n*n,range(10)) #将range(10)中的每个值交给 lambda处理，返回处理结果集
print(d)
print(isinstance(d,Iterator))
for i in d:
    print(i)

print("\r\n========== reduce")
e = functools.reduce(lambda x,y:x+y,range(10)) # 依次将range(10)中的每个值及其下一个值传递给前面的x，y，代表的是一种运算规则
print(type(e))
print(e)

f = functools
print(type(f))
print(f)

print("\r\n========== frozenset")
a = set([1,2,3,3])
print(a)
a = frozenset([1,2,3,3])#不可变集合

print("\r\n========== globals")
print(globals()) #当前整个文件的所有字段


print("\r\n========== ")
print(hash("a"))

print(hash("毕"))

print("\r\n========== ")

print(locals())
print("\r\n========== ")
for i, v in {'q': 'q', 'd': 'd'}.items():
    print(i, v)
print("\r\n========== ")
def test():
    local_var = 333
    print(locals())
    print(globals())
print(globals())
print(locals())
test()
print("\r\n========== max min")
print(max([1,2,4,44,3]))
print(min([1,2,4,44,3]))

print("\r\n========== ")
print(hex(16))  #0x10 16进制
print(oct(16))  #0o20 8进制
print("\r\n========== ")
ord("2")
print("\r\n========== ")

print(reversed([1,2,4,3]))
# print(slice(2))
a = {6:3,1:3,4:5,-1:3,22:2}
print(a)
print(sorted(a.items(),key = lambda x : x[1]))
print("\r\n========== ")

print(sum([1,2,3,5,6]))
print("\r\n========== ")
a = [1,2,3,4]
b = ['a','b','c','d']
print(zip(a,b))
for i in zip(a,b):
    print(i)


print("\r\n========== ")
# import iterator
__import__('iterator')

