class Dog(object):
    def __init__(self):     #只负责初始化
        print("init")

    def __del__(self):
        print("del")

    def __str__(self):
        print("str")
        return "ssss"
    
    def __new__(cls):       #只负责创建   #cls：Dog指向的类
        print("new")
        return object.__new__(cls)

test = Dog()            #调用__new__方法创建对象
