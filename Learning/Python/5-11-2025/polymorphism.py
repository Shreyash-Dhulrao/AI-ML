class Car:
    def __init__(self, brand, model):
        self.__brand = brand # In this the double underscore define about the privacy of the variable. Now we cant directly access this variable outside the class
        self.__model = model

    def get_brand(self):
        return self.__brand
    
class Audi(Car):
    def get_brand(self):
        return super().get_brand()

pr_car = Car("Audi", "E class")
print(pr_car.get_brand())