'''
9-8 权限：编写一个名为 Privileges 的类，它只有一个属性—— privileges ，其中
存储了练习 9-7所说的字符串列表。将方法 show_privileges() 移到这个类中。在 Admin
类中，将一个 Privileges 实例用作其属性。创建一个 Admin 实例，并使用方法
show_privileges() 来显示其权限。
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


class Admin(User):
    def __init__(self, first_name, last_name,privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

p = Privileges(["can add post", "can delete post", "can ban user"])
Admin1 = Admin("Albert", "Einstein",p)
Admin1.privileges.show_privileges()