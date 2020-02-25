'''
9-5 尝试登录次数：在为完成练习 9-3 而编写的 User 类中，添加一个名为
login_attempts 的属性。编写一个名为 increment_login_attempts() 的方法，它将属性
login_attempts 的值加 1。再编写一个名为 reset_login_attempts() 的方法，它将属性
login_attempts 的值重置为 0。
根据 User 类创建一个实例，再调用方法 increment_login_attempts() 多次。打印属
性 login_attempts 的值，确认它被正确地递增；然后，调用方法 reset_login_attempts() ，
并再次打印属性 login_attempts 的值，确认它被重置为 0。
'''


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title())

UserA = User("Albert", "Einstein")
UserA.describe_user()
UserA.greet_user()
print(UserA.login_attempts)
UserA.increment_login_attempts()
UserA.increment_login_attempts()
UserA.increment_login_attempts()
print(UserA.login_attempts)
UserA.reset_login_attempts()
print(UserA.login_attempts)

