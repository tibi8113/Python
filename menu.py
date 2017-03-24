import misfunciones as m
import json

def buscar_zona():
    for z, p in m.zonas.items():
        print(z)
        for d in p:
            if d == destino:
                zona = z
                break
    return zona


def print_zonas():
    for z, p in m.zonas.items():
        print(p)




def print_precios():
    for p in m.precios.values():
        print(p)

mizona = 1
mipoblacion = "Irun"



"""MAIN"""

#opc = input("1.Ida\n2.Ida y vuelta\n3.Mensual\n")
opc = "1"



if opc == "1":
    opc = "ida"
    print("IDA")

elif opc == "2":
    print("IDA Y VUELTA")

elif opc == "3":
    print("MENSUAL")

elif opc =="4":
    print("MENSUAL ILIMITADO")
    
print_zonas()


destino = input()
#destino = "Urnieta"

print("El precio de (" + opc + ") de " + mipoblacion + " a " + destino + " es:")




    
