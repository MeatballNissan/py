
"""
file = open ('bxd.txt','a',encoding="utf-8")#具体见open
# print(type(file.read()))
# print(file.read())
# file.close()
file.write("\n我也爱北京天安门")

for i in range(10):
    print(i)

file.close()

file = open ('bxd.txt','r',encoding="utf-8")#具体见open
#print(file.readlines())

#readlines 只适合读小文件

for i in file: #迭代器，只留一行数据在内存中  可以读大文件
    print(type(i))


#with代码块执行完后 会自动关闭文件流
with open('bxd.txt','r') as file:
    # print(file.readlines())
    for line in file.readlines():
        print(line)

with open('bxd.txt','r') as f1,open('bxd2.txt','r') as f2:
    for line in f1.readlines():
        print(line)

    for line in f2.readlines():
        print(line)
"""



s = "你好"
# print(s.encode("gbk").decode("gbk"))
print(s.encode("gbk"))
print(s.encode())



