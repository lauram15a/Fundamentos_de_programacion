#Laura Mambrilla Moreno
#Ej 7 Cuaderno 6

"""
Realizar un programa que lea desde teclado un número entero positivo y lo
convierta a binario utilizando recursividad.
"""

def binario (n):
    """
    int --> int
    OBJ: pasar n a binario
    """
    if n > 1:
        binario(n//2)
    print (n%2, end='')
        


#main
n = int(input('Número positivo: '))
binario (n)
