#mammal - drink
#Mammal > Human - milk, walk
#Mammal, fish > whale -swim, milk
#mammal > wolf - milk, hunt

class Mammal:
    def __init__(self,name):
        self.name=name
    def feed(self):
        print("{} likes drinking milk".format(self.name))
    def walk(self):
        print("Yes , I can walk")


class Human(Mammal):
    def walk(self, name):
        print("{} can walk ".format(self.name))

class Fish(Human):
    def __init__(self,name):
        self.name=name
    def swim_water(self,name):
        print("Yes , {} can swim".format(self.name))
        print("{} can do a lot of stuff".format(self.name))

class Wolf(Mammal):
    def hunt(self, name):
        print("{} is a hunter. Guys be carefull ^-^".format(self.name))

laika = Wolf("Laika")
laika.feed()
aiza = Human("Biroo")
aiza.feed()
aiza.walk("Biroo")
aiza=Fish("Biroo")
aiza.swim_water("Biroo")
aiza=Wolf("Biroo")
aiza.hunt("Biroo")
