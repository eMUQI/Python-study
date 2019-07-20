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
    def bark(self):
        print("Wang~~~~")
        Dog.bark(self)      #super().bark()

b = Dog()
b.bark()
print()

c = XD()
c.fly()
c.bark()

c.eat()
print()
