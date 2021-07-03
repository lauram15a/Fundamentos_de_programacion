#Laura Mambrilla Moreno
#Ej 8 Cuaderno 6

"""
Calcular la suma de los números pares entre 0 y n de manera recursiva.
"""

def suma_pares (n):
    """
    int --> int
    OBJ: Suma de los números pares en [0,n]
    """
    if n == 0 or n == 1:
        return 0
    elif n%2 == 0:
        return n + (suma_pares(n-2))
    else:
        return n-1 + (suma_pares(n-3))

#main
n = int(input('Introduce un número: '))
print('\n Suma de los números pares en [0,',n,']: ',suma_pares (n))
        
        
