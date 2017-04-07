mizona = 1
mipoblacion = "Irun"
destino = ""
opc = ""

precios = {
    "ida" : [1.70, 1.90, 2.60, 3.35, 3.80, 5.00],
    "ida y vuelta" : [2.60, 2.75, 4.10, 5.50, 6.40, 8.00],
    "mensual" : [34.45, 43.95, 58.65, 73.30, 85.80, 91.00],
    "mensual ilimitado" : [45.60, 51.70, 73.00, 95.85, 109.55, 144.60],
          }

zonas = {
    1 : ["Urnieta","Hernani Centro","Hernani","Martutene","Loiola","Donosti","Gros","Ategorrieta","Intxaurrondo","Herrera","Pasaia","Lezo-Renteria"],
    2 : ["Billabona Zizurki","Andoain Centro","Andoain","Ventas de Irun","Irun"],
    3 : ["Alegia","Tolosa","Tolosa Centro","Anoeta"],
    4 : ["Beasain","Ordizia","Itsasondo","Legorreta","Ikaztegieta"],
    5 : ["Legazpi","Zumarraga","Ormaiztegi"],
    6 : ["Brinkola"],
        }

def buscar_zona():
    for z, p in zonas.items():
        for d in p:
            if d == destino:
                zona = z
                break
        return zona


def print_stations():
    stations = []
    for z, p in zonas.items():
        for s in p:
            stations.append(s)
    return stations

"""def print_zonas():
    stations = ''
    for z, p in zonas.items():
        for s in p:
            stations += '<a href="#">' + s + '</a><br>'
    return stations"""


def print_precios():
    for p in precios.values():
        return p

def get_precio():
    zona_dest = buscar_zona()
    zona = abs(mizona - zona_dest)
    return precios[opc][zona]


