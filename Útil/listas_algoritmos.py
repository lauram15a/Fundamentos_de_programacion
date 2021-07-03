#Librerias
import random

#Funciones
def busqueda_secuencial(lista, item):
    i = 0
    posicion = -1
    while (i<len(lista) and posicion<0):
        if (lista[i] == item):
            posicion = i
        i +=1
    return posicion

def busqueda_binaria(lista, item):
    primero = 0
    ultimo = len(lista)-1
    posicion = -1
    while primero<=ultimo and posicion<0:
        medio = (primero + ultimo)//2
        if lista[medio] == item:
            posicion = medio
        else:
            if item < lista[medio]:
                ultimo = medio-1
            else:
                primero = medio+1
    return posicion

def ordenar_burbuja(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if (lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

#Programa principal
lista = []
for i in range(20):
    lista.append(random.randrange(1,21))
print("Lista inicial:", lista)
pos = busqueda(lista, 15)
if (pos<0):
    print("El elemento no se encuentra en la lista")
else:
    print("El elemento se encuentra en la posición %d"%(pos))

ordenarBurbuja(lista)
print("Lista ordenada:", lista)
pos = busquedaBinaria(lista, 15)
if (pos<0):
    print("El elemento no se encuentra en la lista")
else:
    print("El elemento se encuentra en la posición %d"%(pos))
