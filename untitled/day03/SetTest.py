'''
#列表元组有序
#列表可改， 元组只读

#集合 set 无序不重复
list_1 = [1,2,4,55,3,3]
list_1 = set(list_1)
print()
list_2 = [1,2,11,22,44,3]
#交集
print(list_1.intersection(list_2))
#并集
print(list_1.union(list_2))
#差集
print(list_1.difference(list_2))
list_2 = set(list_2)
print(list_2.difference(list_1))

#判断子集
#判断子集
print(list_1.issubset(list_2))
list_3 = set([1,2])
print(list_2.issuperset(list_1))
print(list_2.issuperset(list_3))

#对称差集（二者完全不同的部分）
print(list_2.symmetric_difference(list_1))

list_2.pop()
list_2.update([1,2])#update
print(list_2)

list_4 = set([1,2])
print(list_4.isdisjoint(list_2))
'''
list_1 = set([1,2,3])
list_2 = set([1,2,4,6])
print(list_1 & list_2)
print(list_1 | list_2)
print(list_2 - list_1)
print(list_2 ^ list_1)

#列表 append insert
list_1.add("55")
print(list_1)
list_1.update(set([55,1,2,"44",44]))
print(list_1)

list_1.remove(44)
print(list_1)

print("44" in list_1)
print("44" not in list_1)

print(set([1]).issubset(list_1))

list_1.discard("xx")
#list_1.remove("xx") remove 不包含会报错 discard不会
print(list_1)








