'''
9-4 就餐人数：在为完成练习 9-1 而编写的程序中，添加一个名为 number_served
的属性，并将其默认值设置为 0。根据这个类创建一个名为 restaurant 的实例；打印有
多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
添加一个名为 set_number_served() 的方法，它让你能够设置就餐人数。调用这个
方法并向它传递一个值，然后再次打印这个值。
添加一个名为 increment_number_served() 的方法，它让你能够将就餐人数递增。
调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+".")
        print("The cuisiner of restaurant is "+self.cuisine_type+".")

    def print_number_served(self):
        print("The number is " + str(self.number_served))

    def open_restaurant(self):
        print(self.restaurant_name+" is open.")

    def set_number_served(self, num):
        self.number_served = num
        print("number_served:"+str(self.number_served))

    def increment_number_served(self, num):
        self.number_served += num


R = Restaurant("Happy", "Chinese food")
R.describe_restaurant()
R.print_number_served()
R.set_number_served(10)
R.print_number_served()
R.increment_number_served(5)
R.print_number_served()
