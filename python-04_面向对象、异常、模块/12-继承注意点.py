class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print("------1-------")
    def __test2(self):
        print("------2-------")
    def test3(self):
        print(self.__num2)
        self.__test2()


class B(A):
    def test4(self):
        print(self.__num2)
        self.__test2()


b = B()
b.test1()
b.test3()
#b.test4()       #无法调用
