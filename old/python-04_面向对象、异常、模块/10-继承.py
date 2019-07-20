class Animal:
    def eat(self):
        print("eating...")
    def drink(self):
        print("drinking...")
    def sleep(self):
        print("sleeping...")
    def run(self):
        print("runing...")

class Dog(Animal):
    def bark(self):
        print("wang...")

class XD(Dog):
    def fly(self):
        print("flying...")

a = Animal()
a.eat()
print()

b = Dog()
b.eat()
b.bark()
print()

c = XD()
c.fly()
c.bark()
c.eat()
print()
