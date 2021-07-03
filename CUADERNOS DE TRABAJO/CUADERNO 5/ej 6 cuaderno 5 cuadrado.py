#Laura Mambrilla Moreno
#Ej 6 cuaderno 5

"""
Implementa una estructura “Cuadrado” que incluya información sobre sus 4
vértices y sobre su punto central, todos los cuales seran del tipo Punto2D.
"""

#librerías
import math

#funciones
class Punto2D :
    def __init__ (self, x, y):
        self.x = x
        self.y = y

class Cuadrado :
    def __init__ (self, v1, v2, v3, v4, centro):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.centro = centro

def crear_punto ():
    """
    nada --> float, float
    OBJ: crear punto
    """
    x = float(input('\nx = '))
    y = float(input('y = '))
    punto = Punto2D(x, y)
    return punto

def crear_cuadrado ():
    """
    nada --> float, float, float, float
    OBJ: crear cuadrado
    """
    print('\n Vértice 1: ')
    v1 = crear_punto ()
    print('\n Vértice 2: ')
    v2 = crear_punto ()
    print('\n Vértice 3: ')
    v3 = crear_punto ()
    print('\n Vértice 4: ')
    v4 = crear_punto ()
    #calculamos centro
    x = (v4.x + v3.x)/2
    y = (v1.y + v3.y)/2
    centro = Punto2D(x, y)
    cuadrado = Cuadrado (v1, v2, v3, v4, centro)
    return cuadrado

def calcular_distancia (punto1, punto2):
    """
    float, float --> float
    OBJ: calcular la distancia entre 2 puntos
    """
    d = math.sqrt((punto2.x - punto1.x)**2 + (punto2.y - punto1.y)**2)
    return d

    
def comprobar_cuadrado (cuadrado):
    """
    float --> bool
    OBJ: comprobar que los datos introducidos forman un cuadrado
    """
    #lados
    #v1 y v2
    d12 = calcular_distancia (cuadrado.v1, cuadrado.v2)
    #v1 y v3
    d31 = calcular_distancia (cuadrado.v3, cuadrado.v1)
    #v2 y v4
    d42 = calcular_distancia (cuadrado.v4, cuadrado.v2)
    #v3 y v4
    d34 = calcular_distancia (cuadrado.v3, cuadrado.v4)
    #diagonales
    #v1 y v4
    d14 = calcular_distancia (cuadrado.v1, cuadrado.v4)
    #v2 y v3
    d23 = calcular_distancia (cuadrado.v2, cuadrado.v3)
    #comprobamos
    return d12 == d31 and d31 == d42 and d42 == d34 and d14 == d23

def mostrar_cuadrado (cuadrado):
    """
    float --> float
    OBJ: imprimir las coordenadas del cuadrado
    """
    print('\n COORDENADAS CUADRADO:')
    print ('v1 = (', cuadrado.v1.x,',',cuadrado.v1.y,')')
    print ('v2 = (', cuadrado.v2.x,',',cuadrado.v2.y,')')
    print ('v3 = (', cuadrado.v3.x,',',cuadrado.v3.y,')')
    print ('v4 = (', cuadrado.v4.x,',',cuadrado.v4.y,')')
    print ('centro = (', cuadrado.centro.x,',',cuadrado.centro.y,')')
    

#main
    
print ('\n   v1-----------v2')
print ('   |             |')
print ('   |             |')
print ('   |             |')
print ('   |             |')
print ('   |             |')
print ('   |             |')
print ('   v3-----------v4 ')
cuadrado = crear_cuadrado ()

if comprobar_cuadrado(cuadrado) == True:
    mostrar_cuadrado (cuadrado)
else:
    print('\nNo es un cuadrado.')
    

    
    
            
