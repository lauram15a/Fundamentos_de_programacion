
#Ejercicio 13 - Cuaderno 2
#Escribe una función que a partir de las coordenadas 3D de dos puntos en el espacio en formato (x, y, z) calcule la distancia que hay entre dichos puntos.Prueba su función y el resultado por pantalla.


import math



def distancia (xA, yA, zA, xB, yB, zB):
    """
    float, float, float ---> float
    OBJ: calcular la distancia entre 2 puntos en el espacio
    """
    distancia = math.sqrt ((xB - xA)**2 + (yB - yA)**2 + (zB - zA)**2)
    return distancia

#PROBADOR
print ('Punto A')
xA = float (input( 'x = '))
yA = float (input( 'y = '))
zA = float (input( 'z = '))

print (' ')

print ('Punto B')
xB = float (input( 'x = '))
yB = float (input( 'y = '))
zB = float (input( 'z = '))

print (' ')
print ('Distancia entre A y B = ', distancia (xA, yA, zA, xB, yB, zB), ' unidades')

