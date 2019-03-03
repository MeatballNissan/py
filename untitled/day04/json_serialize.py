#
# f = open('bxd.txt','w')
# f.write("aaaa")
# a = {'a':'a','b':'b'}
# f.write(str(a))

# f = open('bxd.txt','r')
# s = f.readline()
# print(type(eval(s)))
import pickle

import json
def syaHi(name):
    print("hello",name)

dict = {'a':'a','b':'b','c':syaHi}

f = open('bxd_json.txt','w')
# print(json.dumps(dict))

# f.write(json.dumps(dict))
f = open('bxd_json.txt','r')
# data = json.loads(f.read())
# print(data)

# print(type(data))

# print(json.dumps(dict))

f = open('pickle.txt','wb')

print(pickle.dumps(dict))
# f.write(pickle.dumps(dict))
pickle.dump(dict,f)

f = open('pickle.txt','rb')
# data = pickle.loads(f.read())
data = pickle.load(f)
print(data['c']('a'))
