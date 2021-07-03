#Laura Mambrilla Morneo
#Ej 7 cuaderno 5

"""
Haciendo uso de lo programado en ejercicios anteriores, programe una
función que dilucide si un cuadrado es mayor que otro.
"""

#librerías
import math

#funciones
class Punto2D :
    def __init__ (self, x, y):
        self.x = x
        self.y = y

class Cuadrado :
    def __init__ (self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4

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
    cuadrado = Cuadrado (v1, v2, v3, v4)
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

def mostrar_cuadrado_1 (cuadrado1):
    """
    float --> float
    OBJ: imprimir las coordenadas del cuadrado
    """
    print('\nCOORDENADAS CUADRADO 1:')
    print ('v1 = (', cuadrado1.v1.x,',',cuadrado1.v1.y,')')
    print ('v2 = (', cuadrado1.v2.x,',',cuadrado1.v2.y,')')
    print ('v3 = (', cuadrado1.v3.x,',',cuadrado1.v3.y,')')
    print ('v4 = (', cuadrado1.v4.x,',',cuadrado1.v4.y,')')

def mostrar_cuadrado_2 (cuadrado2):
    """
    float --> float
    OBJ: imprimir las coordenadas del cuadrado
    """
    print('\nCOORDENADAS CUADRADO 2:')
    print ('v1 = (', cuadrado2.v1.x,',',cuadrado2.v1.y,')')
    print ('v2 = (', cuadrado2.v2.x,',',cuadrado2.v2.y,')')
    print ('v3 = (', cuadrado2.v3.x,',',cuadrado2.v3.y,')')
    print ('v4 = (', cuadrado2.v4.x,',',cuadrado2.v4.y,')')
    

#main
    
print ('\n   v1-----------v2')
print ('   |             |')
print ('   |             |')
print ('   |             |')
print ('   |             |')
print ('   |             |')
print ('   |             |')
print ('   v3-----------v4 ')

print('\n----------')
print('CUADRADO 1')
print('----------')
cuadrado1 = crear_cuadrado ()
cuadrado = cuadrado1
lado_1 = calcular_distancia (cuadrado.v3, cuadrado.v1)

if comprobar_cuadrado(cuadrado) == True:
    print('\n----------')
    print('CUADRADO 2')
    print('----------')
    cuadrado2 = crear_cuadrado ()
    cuadrado = cuadrado2
    lado_2 = calcular_distancia (cuadrado.v3, cuadrado.v1)
    if comprobar_cuadrado(cuadrado) == True:
        area_1 = math.pow(lado_1, 2)
        area_2 = math.pow(lado_2, 2)
        if area_1 < area_2:
            print('\n--------------------------------------')
            print('El 2º cuadrado introducido es el mayor.')
            mostrar_cuadrado_2 (cuadrado2)
        elif area_1 > area_2:
            print('\n--------------------------------------')
            print('El 1º cuadrado introducido es el mayor.')
            mostrar_cuadrado_1 (cuadrado1)
        else:
            print('Ambos cuadrados tienen las mismas dimensiones.')
    else:
        print('\nNo es un cuadrado.')
else:
    print('\nNo es un cuadrado.')
