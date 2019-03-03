
info = {'a': "=adfdsfs", 'b': 'bbbbbb'}
print(info.get("a"))
print(info.values())
print(info.keys())
#info.popitem()
print(info.items())
c = dict.fromkeys([1, 2, 3], ["a", "b", "c"])
print(c)
c.get(1)[0] = "e"
print(c) # 1,2,3的数据都被改掉了 说明存的是地址值

#dict 遍历 方式一 快
for i in info:
    print(i, info[i])
#dict 遍历 方式二 慢，因为先把dict转为了元组
for k,v in info.items():
    print(k, v)
