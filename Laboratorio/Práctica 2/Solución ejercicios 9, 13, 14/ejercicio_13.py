'''
Cuaderno de trabajo 2.pdf - Ejercicio 13

Descripción: Calcular la distancia entre dos puntos en 3D.
'''
#Librerías
import math

#Funciones
def distancia3D(p1x,p1y,p1z,p2x,p2y,p2z):
    ''' float,float,float,float,float,float --> float
        OBJ: Distancia entre dos puntos'''
    dist = math.sqrt((p2x-p1x)**2 + (p2y-p1y)**2 + (p2z-p1z)**2)
    return dist


#Programa principal
p1x = float(input("Punto 1 (x): "))
p1y = float(input("Punto 1 (y): "))
p1z = float(input("Punto 1 (z): "))

p2x = float(input("Punto 2 (x): "))
p2y = float(input("Punto 2 (y): "))
p2z = float(input("Punto 2 (z): "))

distancia = distancia3D(p1x,p1y,p1z,p2x,p2y,p2z)

print("\nLa distancia que hay entre los puntos es: %.4f" %distancia)
