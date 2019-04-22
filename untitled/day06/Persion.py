class Persion:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        print("taking",self.name,self.age)

persion = Persion("bxd","18")
print(persion.name)
persion.talk()

class Relation(object):
    def make_friends(self, obj):
        print("%s is making friends with %s" %(self.name ,obj.name))


class Man(Persion,Relation):
    def piao(self):
        print("piao  ....")


man = Man("bxd1",19)
man.talk()
man.piao()
man2 = Man("bxd2",19)
man.talk()
man.piao()


class Woman(Persion):
    def shoping(self):
        print("shoping ...")


woman = Woman("dsfad",29 )
woman.talk()
woman.shoping()

#上述Persion为经典类
#新式类
class People(object):
    def __init__(self, name):
        self.name = name
        super(People, self).__init__(name) #新式类

print(man.make_friends(man2))

# 多继承查找
# 1. 广度优先  优先找多继承的类 （python3开始  经典和新式都是广度优先）  2.深度优先，优先找第一个继承类的父类（python2 经典类深度优先，新式类广度优先）


