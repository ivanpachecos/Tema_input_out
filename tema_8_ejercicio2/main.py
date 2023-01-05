"""
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una
clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
"""
from pickle import *


# Creamos la clase Vehiculo con algunos datos
class Vehiculo():
    marca = ""
    color = ""  # Los valores quedaran vacios por el momento
    puertas = 0

    # Funcion principal
    def __init__(self, marca, color, puertas):
        self.marca = marca
        self.color = color
        self.puertas = puertas

    # Para que devualva y poder mostrar por pantalla
    def __str__(self):
        return f'El coche es un {self.marca} de color {self.color} que tiene {self.puertas} puertas'


# Asignamos en una variable para despúes imprimirlo
v = Vehiculo('Audi', 'Blanco', 5)
print(str(v))

f = open('class_vehiculo.txt', 'w+b')
dump(v, f)

f.seek(0)
save_file = load(f)

print(save_file)
f.close()
