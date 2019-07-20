class CarStore(object):
    def __init__(self):
        self.factory = Factory()

    def order(self,car_type):
        k = self.factory
        f = k.select_car_by_type(car_type)
        return f

class Factory(object):
    def select_car_by_type(self,car_type):
        if car_type == "suonata":
            return Suonata()
        elif car_type == "mingtu":
            return Mingtu()
        elif car_type == "ix25":
            return Ix35()

class Car(object):
    def move(self):
        print("moving...")
    def music(self):
        print("lalala...")
    def stop(self):
        print("stop")

class Suonata(Car):
    pass

class Mingtu(Car):
    pass

class Ix35(Car):
    pass


car_store = CarStore()
car = car_store.order("ix25")
car.move()
car.music()
car.stop()

