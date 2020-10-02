class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("Bow Bow!!")
        
class Cat(Mammal):
    def meow(self):
        print("Meow Meow!!")

d1 = Dog()
c1 = Cat()
d1.walk()
c1.meow()
