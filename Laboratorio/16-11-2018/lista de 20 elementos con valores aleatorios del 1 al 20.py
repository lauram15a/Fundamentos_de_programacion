#Clase 16/11/2018

#1- Crear lista de 20 elementos con valores aleatorios del 1 al 20
#2- Hacer una función que devuelva la posición que ocupa un elemento o -1
#3- Ordenar la lista 

import random

def buscar (lista, elem):
    i = 0
    pos = -1
    while (i<len(lista) and pos<0):
        if (lista[i] == elem):
            pos = i
        i += 1
    return pos

def ordenar (lista): #método de la burbuja
    for i in range (len(lista)):
        for j in range (i+1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

#main
lista = []
for i in range (20):
    lista.append(random.randrange(1,21))
print ('\n Lista inicial: ', lista)
elem = int(input('Elemento a buscar: '))
pos = buscar (lista, elem)
print ('Posición de ',elem, ':',pos)
#ordenar lista
lista2 = lista[:] #copiar lista
lista.sort() #ordenar lista con .sort
print('Lista ordenada:',ordenar(lista2)) #ordenar lista por método burbuja

