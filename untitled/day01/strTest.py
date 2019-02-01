
name = "bxd"

fort = "hello {name} ,age {age}"
print(name.capitalize())
print(name.count("x"))
print(name.casefold())
print(name.center(40,"-"))
print(name.endswith("d"))
print(fort.format(name="bxd",age= 22))
print(name.isalnum())#英文字符 + 0-9
print(name.isalpha())#纯英文字符（含大小写）
print("12".isdecimal())#是否为十进制
print(name.isdigit())#是否为数字
print(name.isidentifier())#判断是否为合法标识符（变量名）
print(name.islower())
print(name.isupper())
print(name.isnumeric())# 正则0-9
print(name.isspace())
print("My Name".istitle())#每个单词首字母大写
print(name.isprintable())#可否打印，无用 tty file，drive file

print(name.join("==+-"))#在后面每个字符中间加前面的字符
print(name.join(['1','2','3']))
print(name.ljust(20,"-"))
print(name.rjust(20,"-"))
print(name.lstrip())#去掉左边的空格和回车
print(name.rstrip())#右边
print(name.strip())
p = str.maketrans("abcdef", '123456')
print(p) # p 对应关系
print("bxdabcdef".translate(p))

print(name.replace("x","X"))

print("abcda".rfind("a"))#最右一个匹配的下表

print("aBcd".swapcase())#大小写互换

print("abc".zfill(10))#0补位






