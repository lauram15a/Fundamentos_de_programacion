#Laura Mambrilla Moreno
#Ej 4 Cuaderno 6

"""
Programar, haciendo uso de la recursividad, una función en Python que
permita obtener el término de orden n de la sucesión de Fibonacci
"""

def fibonacci (n):
    """
    int --> int
    OBJ: calcular el número en la posición n de la serie Fibonacci
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n= int(input('\nPosición serie Fibonacci= '))
print(fibonacci (n))
        
    
