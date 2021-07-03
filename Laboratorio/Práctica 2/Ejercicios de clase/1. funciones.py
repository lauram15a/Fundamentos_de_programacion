#Ejercicio 4

#Librerias
import math

#Funciones
def area_circulo(radio):
    """ float --> float
    OBJ: Calcula el area de un circulo
    PRE: radio >= 0 """
    area = math.pi * radio**2
    return area

def perimetro_circunferencia(radio):
    """ float --> float
    OBJ: Calcula el perimetro de una circulferencia
    PRE: radio >= 0 """
    perimetro = math.pi * radio * 2.0
    return perimetro

#Programa principal
radio = float(input('Introduce el valor del radio: '))
print ('área = %.4f' %area_circulo(radio))
print ('perímetro = %.4f' %perimetro_circunferencia(radio))
