class Vehiculo():
    color = ""
    luces = None

    def __init__(self, color, luces):
        self.color = color
        self.luces = luces

    def __repr__(self):
        return f'El color del Vehículo es: {self.color}'

v = Vehiculo('Azul', True)
print(v)