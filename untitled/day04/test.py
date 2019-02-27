#

print(range(10))

for i in range(10):
    print(i)

def func(i):
    print(i*100)

# 列表生成式
[func(i) for i in range(10)]
[print(i*2) for i in range(10)]
print([i * 2 for i in range(10)])
a = [i * 2 for i in range(1)]
print(len(a))


# 生成器   列表生成式会把所有数据准备好，生成器只有在用到的时候才生成，省内存
#生成的列表可以支持切片  生成器不行
(i * 2 for i in range(10))
print((i *2 for i in range(100)))  #<generator object <genexpr> at 0x040582A0>

b = ((i * 2 for i in range(1000)))

# for i in b:
#     print(i)
#print(b[1000])
#生成器只保留当前值
print(b.__next__())
print(b.__next__())
print(b.__next__())
#一般用循环遍历生成器

