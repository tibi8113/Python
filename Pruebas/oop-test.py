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

    def add_fuel(self, amount):
        """Add fuel to the tank."""
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel to "+ self.make + ".")
        else:
            print("The tank won't hold that much.")

""" Crear los objetos """
my_car = Car('Audi' , 'A4' , 2015 , 'Red')
my_car2 = Car('Ford' , 'Mustang' , 2016)

my_car.add_fuel(50)

print(my_car)
print(my_car2)



#print("Make: " + my_car.make + "; " + "Model: " + my_car.model + "; " + "Color: " + my_car.color)
#print("Make: " + my_car2.make + "; " + "Model: " + my_car2.model + "; " + "Color: " + my_car2.color)
