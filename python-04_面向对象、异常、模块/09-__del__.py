import sys

class Dog:
    def __del__(self):          #类似析构数
        print("gg")

dog1 = Dog()
print(sys.getrefcount(dog1))
dog2 = dog1
print(sys.getrefcount(dog1))

print()
print(dog1)
print(dog2)

del dog1
print(sys.getrefcount(dog2))
print(50*"=")
print(dog2)
del dog2
print(50*"=")
