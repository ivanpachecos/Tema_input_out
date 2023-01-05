"""
Str para salida informales
"""
class Juguete():
    nombre = ""
    precio = 0.00

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    #Sobrecargar métodos
    def __str__(self):
        return f'El juguete es {self.nombre} y su precio es {self.precio}'

dem = Juguete("Mono", 12.3)

print(dem)