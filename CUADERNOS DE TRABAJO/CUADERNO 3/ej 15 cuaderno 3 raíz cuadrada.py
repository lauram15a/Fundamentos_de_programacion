
#EJERCICIO 15

"""
Obtén las raíces de una ecuación de segundo grado a*x**2 + b*x + c = 0 a partir de
sus coeficientes a, b y c. Recuerda que si el discriminante es cero la raíz es única
(-b/2xa) y que si el discriminante es negativo las raíces son imaginarias, en cuyo
caso deberá indicarse con un mensaje “raíces imaginarias”.

"""

import math

a= float(input('a = '))
b= float(input('b = '))
c= float (input('c = '))

def raiz (a,b,c):
    """
    int, int, int --> int
    OBJ: calcular las raíces
    """
    discriminante= b**2 - 4 * a * c
    if discriminante == 0:
        raiz_unica= (-b) / (2 * a)
        return 'Raíz única = ', raiz_unica
    if discriminante < 0:
        return 'Raíces imaginarias'
    raiz_mas= (-b + math.sqrt(discriminante)) / (2 * a)
    raiz_menos= (-b - math.sqrt(discriminante)) / (2 * a)
    
    return raiz_menos , raiz_mas

print (raiz(a,b,c))
