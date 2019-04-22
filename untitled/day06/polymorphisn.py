
class Animal(object):
    def __init__(self, name):
        self.name = name
    def talk(self):
        return ""
    @staticmethod
    def animal_talk(obj: object) -> object:
        obj.talk()
class Dog(Animal):
    def talk(self):
        print("wang wang")
class Cat(Animal):
    def talk(self):
        print("miao")

d = Dog("dog")


c = Cat('cat')

def animal_talk(obj: object) -> object:
    obj.talk()

animal_talk(d)
animal_talk(c)

Animal.animal_talk(d)
Animal.animal_talk(c)

