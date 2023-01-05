"""
Salida técnica 
"""
class Jugeute():
    nombre = ""
    precio = 0.00

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f'{self.nombre} su valor es {self.precio}'

total = Jugeute("Cerdo", 8.40)
print(total)