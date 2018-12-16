class Dog:
    def __init__(self,n):
        self.__name = n
    def test1(self):
        print(6*"w")
    def test2(self):
        print(5*"-"+"w"+5*"-")
        self.__test()
    def __test(self):
        print(self.__name+"汪！")    

dog = Dog("jack")
dog.test1()
dog.test2()
#print(dog.__name)      外界无法调用
#dog.__test()           外界无法调用
