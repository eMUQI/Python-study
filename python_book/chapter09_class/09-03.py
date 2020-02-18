'''
9-3 用户：创建一个名为 User 的类，其中包含属性 first_name 和 last_name ，还有
用户简介通常会存储的其他几个属性。在类 User 中定义一个名为 describe_user() 的方
法，它打印用户信息摘要；再定义一个名为 greet_user() 的方法，它向用户发出个性化
的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
'''


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)


    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title())


UserA = User("Albert", "Einstein")
UserA.describe_user()
UserA.greet_user()
