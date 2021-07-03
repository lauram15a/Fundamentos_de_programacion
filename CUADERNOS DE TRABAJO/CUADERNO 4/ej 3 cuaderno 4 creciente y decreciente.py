#Laura Mambrilla Moreno
#Ejercicio 3 Cuaderno 4

"""
Distribuir los 20 datos enteros en dos listas de tal manera que se vayan
generando dos secuencias ordenadas, una creciente y otra decreciente.
"""
#librerías
import random

import random

#funciones

import random

#funciones

def llenar_lista_principal():
    """
    list --> list
    OBJ: llenar la lista 
    """
    n= 20
    lista = [0] * n
    for i in range(n):
        lista[i] = random.randint(0,90)
    return lista

def creciente (lista):
    """
    list --> list
    OBJ: ordenar la lista crecientemente
    """
    listacreciente = lista[:]
    #método de la burbuja
    n = len(listacreciente)
    for i in range(n-1):
        for j in range(i+1,n):
            if listacreciente[i] > listacreciente[j]:
                listacreciente[i],listacreciente[j] = listacreciente[j],listacreciente[i]
    return listacreciente


def decreciente (lista):
    """
    list --> list
    OBJ: ordenar la lista decrecientemente
    """
    #método de la burbuja
    n = len(lista)
    for i in range(n-1):
        for j in range(i+1,n):
            if lista[i] < lista[j]:
                lista[i],lista[j] = lista[j],lista[i]
    return lista

#main
lista = llenar_lista_principal()
print (lista)
print ('creciente:', creciente (lista))
print ('decreciente:',decreciente (lista))
