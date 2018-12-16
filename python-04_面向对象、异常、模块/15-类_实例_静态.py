class Test(object):
    #类属性
    num = 0

    #实例方法
    def __init__(self):
        #实例属性
        self.name = "test"

    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 180

    #静态方法
    @staticmethod
    def printit():
        print(5*"test\n")

test = Test()
#Test.add_num()
test.add_num()
print(Test.num)

Test.printit()
#game.printit()
