class Persion:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        print("taking",self.name,self.age)

persion = Persion("bxd","18")
print(persion.name)
persion.talk()

class Man(Persion):
    def piao(self):
        print("piao  ....")


man = Man("bxd1",19)
man.talk()
man.piao()


class Woman(Persion):
    def shoping(self):
        print("shoping ...")


woman = Woman("dsfad",29 )
woman.talk()
woman.shoping()
