class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__color = 'red'
        self.fuel_capacity = 20
        self.fuel_level = 0


""" Crear los objetos """
my_car = Car('Audi' , 'A4' , 2015 , color)
my_car2 = Car('Ford' , 'Mustang' , 2016)
my_car3 = Car('Audi' , 'RS6' , 2017)

print("Make: " + my_car.make + "; " + "Model: " + my_car.model)
print("Make: " + my_car2.make + "; " + "Model: " + my_car2.model)
print("Make: " + my_car3.make + "; " + "Model: " + my_car3.model)