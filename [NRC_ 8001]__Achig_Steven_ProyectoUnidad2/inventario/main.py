#import Martillo
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Producto:
    marca = 'DeWalt'
    cantidad = 0
    precio = 0
    def __init__(self, a, b):
        self.vender = a + b - 1
        self.comprar = a - b + 1
        self.eliminado = a /b - 1
        self.editado = a*b + 1
    pass

"""
martillo = Producto()
destornillador = Producto()

#objeto.atributo = valor
martillo.precio = 12.89
martillo.cantidad = 15
martillo.marca = 'Stanley'

destornillador.precio = 1.35
martillo.cantidad = 24
martillo.marca = 'DeWalt'
"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    martillo = Producto(2, 4)
    print("Se ha vendido un martillo: ", martillo.vender)
    print("El precio es: ", getattr(martillo, 'precio'))
    print("El martilloo tiene una marca?: ", hasattr(martillo, 'marca'))