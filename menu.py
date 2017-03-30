import misfunciones as m
import json


"""MAIN"""

opc = input("1.Ida\n2.Ida y vuelta\n3.Mensual\n")

if opc == "1":
    opc = "ida"
    print("IDA")

elif opc == "2":
    print("IDA Y VUELTA")

elif opc == "3":
    print("MENSUAL")

elif opc =="4":
    print("MENSUAL ILIMITADO")
    
print (m.print_zonas())

m.destino = input("Destino: ")

print("El precio de (" + opc + ") de " + m.mipoblacion + " a " + m.destino + " es:")

m.get_precio()





    
