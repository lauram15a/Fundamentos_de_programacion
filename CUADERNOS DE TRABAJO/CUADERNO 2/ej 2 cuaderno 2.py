#Ejercicio 2 - Cuaderno 2

"""
Implementa un programa modularizado que, leyendo de teclado los valores
necesarios, muestre en pantalla el área de un círculo, un cuadrado y un
triángulo. Utiliza el valor 3.1416 como aproximación de П (pi) o importa el
valor del módulo “math”.
"""

import math

print ('Círculo')
radio= float (input('Radio = '))

print ('')

print ('Cuadrado')
lado= float (input('Lado = '))

print ('')

print ('Triángulo')
base= float (input('Base = '))
altura= float (input('Altura = '))

def area_circulo (radio):
    """
    float --> float
    OBJ: calcular área círculo
    """
    area_circulo = math.pi * radio**2
    return area_circulo

print ('Área círculo = ', area_circulo(radio))

def area_cuadrado (lado):
    """
    float --> float
    OBJ: calcular área cuadrado
    """
    area_cuadrado= lado**2
    return area_cuadrado

print ('Área cuadrado = ', area_cuadrado(lado))

def area_triangulo (base, altura):
    """
    float --> float
    OBJ: calcular área triángulo
    """
    area_triangulo = base * altura /2
    return area_triangulo

print ('Área triángulo = ', area_triangulo(base, altura)) 
