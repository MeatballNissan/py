__author__ = "bxd"


class Dog:

    def __init__(self, name):
        self.name = name

    def bulk(self):
        print(" %s :wang wang wang" % self.name)


d1 = Dog("bxd1")
d2 = Dog("bxd2")
d3 = Dog("bxd3")

d1.bulk()
d2.bulk()
d3.bulk()

roles = {
    1:{},2:{}
}

class Role():
    n = 123 # 类变量
    def __init__(self,name,role,gun,n): #构造函数
        self.name = name
        self.gun = gun;
        self.role = role
        self.n = n

    def buy_gun(self,gun_name):
        print("%s just bought %s" %(self.name,gun_name))
        self.gun_name = gun_name;
        self.gun = gun_name
        self.__value = gun_name #私有属性
    def __show_value(self): #私有方法
        print(self.__value)
    def __del__(self):
        print("自动销毁了")

r1 = Role("bxd", "terrorist", "c43","321")

print(r1.gun)
print(r1.name,r1.role)
r1.buy_gun("ak47")
print(r1.gun_name, r1.gun )
print(r1)
print(r1.n)
print(Role.n)
r1.n = 3214  # 改类变量只能通过 类名.n = 1234 的方式调用
print(Role.n)
del r1
print(111)
#r1 = Role("bxd", "terrorist", "c43")
# 初始化过程 Role(r1,"bxd", "terrorist", "c43")  r1即self， 所以初始化为将r1 传入构造函数，然后给r1这个内存地址中的变量赋值
















