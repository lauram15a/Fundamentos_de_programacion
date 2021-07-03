#Librerías
import sys

#Funciones
def producto(n1, n2):
    ''' int, int -> int
    OBJ: Calcula producto sin utilizar *'''
    prod = 0
    for i in range(n2):
        prod = prod + n1
    return prod

#Programa principal
try:
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
except ValueError:
    print("Error: el valor introducido debe ser un número")
    sys.exit(-1)

resul = producto(n1, n2)
print("\nEl producto es: %d"%(resul))
