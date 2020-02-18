'''
9-7 管理员：管理员是一种特殊的用户。编写一个名为 Admin 的类，让它继承你为
完成练习 9-3 或练习 9-5 而编写的 User 类。添加一个名为 privileges 的属性，用于存
储一个由字符串（如 "can add post" 、 "can delete post" 、 "can ban user" 等）组成的
列表。编写一个名为 show_privileges() 的方法，它显示管理员的权限。创建一个 Admin
实例，并调用这个方法。
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
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)

Admin1 = Admin("Albert", "Einstein")
Admin1.show_privileges()