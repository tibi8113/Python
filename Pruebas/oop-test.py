class Car():

    def __init__(self, make, model, year, color='White'):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_capacity = 100
        self.fuel_level = 0

    def __str__(self):
        return "Car - Make: %s, Model: %s, Color: %s, Fuel: %s" % (self.make, self.model, self.color, self.fuel_level)

    #Repostar
    def add_fuel(self, amount):
        """Add fuel to the tank."""
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel to "+ self.make + ".")
        else:
            print("The tank won't hold that much.")

class ElectricCar(Car):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
        #Tamaño de la bateria.
        self.battery_size = 100
        #Nivel de bateria en %.
        self.charge_level = 0

class WareHouse():
    def __init__(self, name, location)
        self.name = name
        self.location = location
        self.cars = []

    #Añadir un coche.
    def add_car(self, car):
        self.cars.append(car)

    #Quitar un coche.
    def remove_car(self, car):
        self.cars.append(car)


"""-----------------------------------------------------------------------------------------------------------------------------------"""

""" Crear coches """
my_car = Car('Audi' , 'A4' , 2015 , 'Red')
my_car2 = Car('Ford' , 'Mustang' , 2016)
my_electric_car = ElectricCar('Tesla' , 'S' , 2016, 'Cian')

"""-----------------------------------------------------------------------------------------------------------------------------------"""

""" Crear metodos """
my_car.add_fuel(50)

"""-----------------------------------------------------------------------------------------------------------------------------------"""

print(my_car)
print(my_car2)

#Lista de coches
lista_coches = []
lista_coches.append(my_car)
lista_coches.append(my_car2)

#Print de todos los coches
for coche in lista_coches:
    print(coche)

#print("Make: " + my_car.make + "; " + "Model: " + my_car.model + "; " + "Color: " + my_car.color)
#print("Make: " + my_car2.make + "; " + "Model: " + my_car2.model + "; " + "Color: " + my_car2.color)
