#Laura Mambrilla Moreno
#Ej 5 cuaderno 5

"""
Programa una función distancia_2D que calcule la distancia entre dos
puntos. La función retornará un número real según la siguiente fórmula:
d=((x2 - x1)**2 + (y2 + y1)**2)**(1/2)
"""
#librerías
import math

#funciones

class Punto2D :
    def __init__ (self, x, y):
        self.x = x
        self.y = y

def crear_punto ():
    """
    nada --> float, float
    OBJ: crear punto
    """
    x = float(input('\nx = '))
    y = float(input('y = '))
    punto = Punto2D(x, y)
    return punto

def distancia (punto1, punto2):
    """
    float, float --> float
    OBJ: calcular la distancia entre 2 puntos
    """
    d = math.sqrt((punto2.x - punto1.x)**2 + (punto2.y - punto1.y)**2)
    return d

#main
punto1 = crear_punto()
punto2 = crear_punto()
print('\nLa distancia es de %d unidad(es).'%distancia(punto1, punto2))
