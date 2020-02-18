'''
9-1 餐馆：创建一个名为 Restaurant 的类，其方法 __init__() 设置两个属性：
restaurant_name 和 cuisine_type 。创建一个名为 describe_restaurant() 的方法和一个
名为 open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，
指出餐馆正在营业。
根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述
两个方法。
'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+".")
        print("The cuisiner of restaurant is "+self.cuisine_type+".")

    def open_restaurant(self):
        print(self.restaurant_name+" is open.")


new_restaurant = Restaurant("Happy Restaurant", "Chinese food")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
