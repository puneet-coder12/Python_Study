class Car:
    # brand = None, model = None
    
    total_car = 0  # like a static variable
    def __init__(self, brand, model):
        self.__brand = brand  # __ this make the variable private
        self.__model = model
        # self.total_car +=1
        Car.total_car +=1
        
    def get_brand(self):
        return self.__brand
    
    def display(self):
        print("Brand : ", self.__brand, "Model : ", self.__model);
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    @staticmethod   # it is decorator
    def general_desc():
        return "Cars are means of transport"
    
    def model(self):
        return self.__model
    

class Electric(Car):   # in this line it inherit the property of Car
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def full_name(self):
        return super().full_name() + self.battery_size;
    
class Battery:
    def battery_info(self):
        return "This is battery"
    
class Engine():
    def engine_info(self):
        return "This is engine"
    
class ELectricCar(Battery, Engine, Car):
    pass

ev = ELectricCar("Tesla", "Model S")
print(ev.battery_info())
print(ev.full_name())

class Nothing:
    pass   # if you want to leave class, func or if empty then write this mean leave this like this syntaxically
    
my_car = Car("BMW", "EV") #obj Car
my_new_car = Car("Audi", "Petrol")

# print(my_car.model())

# print(my_car.__brand)
# print(my_car.full_name())
# my_car.display()
# my_new_car.display()

electric_car = Electric("Tesla", "Model S", "100kWh")

# print(electric_car.full_name())

print(isinstance(electric_car, Car))
print(isinstance(electric_car, Electric))