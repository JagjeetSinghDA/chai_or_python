class Car:
    # these are class vriables and we cann call them directly by using class name
    total_car = 0 

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1 


# to make it private we use two under scores before the attribute 
# and we have created a new method to call that attribute 
# this is called encapusalation
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand}: {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"
    
    # this is called static method
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    # property makes it private
    @property
    def model(self):
        return self.__model

# my_car = Car("Toyota", "Corola")
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.full_name())


# inheritance
# we can use super() to call the methods from the parent class and use them
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) 
        self.batter_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

# my_tesla = ElectricCar("Tesla", 'Model S', "85KWh")
# print(my_tesla.brand, my_tesla.model, my_tesla.full_name())
# print(my_tesla.__brand)
# print(my_tesla.get_brand())

# just to check the instnce if it is belong to car or electriccar
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# we can use the same method in both the calsses, but when we call the method from the class it gives different results
# this is called polymorphism
# my_car = ElectricCar("Tata", "Safari", "85Kwh")
# print(my_car.get_brand(), my_car.fuel_type())
# mycar = Car("Tata", "Safari")
# mycar.model = "Harrier"
# print(mycar.get_brand(), mycar.model, mycar.full_name(), mycar.fuel_type(), sep = '\n')
# print(mycar.__model)



# print(Car.total_car)
# i didn't understand the statis method bcoz it is still working with the instances and the direct with the class.
# print(mycar.general_description())  
# print(Car.general_description())






class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass 

my_new_tesla = ElectricCarTwo("Tesla", "Model S")

print(my_new_tesla.engine_info(), my_new_tesla.battery_info(), sep = '\n')