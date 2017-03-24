class Perro():
    """ Clase Perro """
class Dog():
    """ Clase Dog """

    def __init__(self, name):
        """ Init Perro """
        self.name = name

    def sit(self):
        """ Sentar al perro """
        print(self.name + " Es un gran perro!")

class SARDog(Dog):
    """ SARDog class """
    def __init__(self, name):
        super.__init__(name)

    def search(self):
        """ Simulacion de busqueda """
        print(self.name + "esta buscando")

    def die(self):
        """ Simulacion de muerte """
        print(self.name + "esta muerto.")

myperro = SARDog("Beltza")
myperro.search()
myperro.sit()
myperro.die()

#print(myperro.name)
#myperro.sit()