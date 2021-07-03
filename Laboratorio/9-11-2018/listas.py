#Crear lista
lista = [10, 20, 30, 40]
print(lista)

#Crear lista de 10 elementos con el valor 0
print('\nCrear lista de 10 elementos con el valor 0')
#Forma 1
lista = [0] * 10
#Forma 2
lista = []
for i in range(10):
    lista.append(0)
print(lista)

#Acceder a un elemento
print('\nAcceder a un elemento')
lista = [10, 20, 30, 40]
print(lista[2])

#Cambiar el valor de un elemento
print('\nCambiar el valor de un elemento')
lista[2] = 25
print(lista)

#Recorrer lista donde i toma cada valor
print('\nRecorrer lista donde i toma cada valor')
for i in lista: 
    print(i)
    
#Recorrer lista donde i es el índice
print('\nRecorrer lista donde i es el índice')
for i in range(len(lista)):
    print(i, lista[i])

#Concatenar listas
print('\nConcatenar listas')
lista = lista + [50]
print(lista)

#Igualar listas
print('\nIgualar listas')
lista2 = lista
lista[0] = 1
print(lista)
print(lista2)

#Subrango
print('\nSubrango')
lista2 = lista[0:2]
print(lista2)

#Copiar lista
print('\nCopiar lista')
lista2 = lista[:]
lista[0] = 10
print(lista)
print(lista2)

#Recorrer lista al revés
print('\nRecorrer lista al revés')
for i in range(len(lista)-1, -1, -1):
    print(i, lista[i])
for i in reversed(range(len(lista))):
    print(i, lista[i])

#Eliminar un valor
print('\nEliminar un valor')
del lista[0]
print(lista)

#Eliminar valores menores o iguales que 30
print ('\nEliminar valores menores o iguales que 30')
for i in range(len(lista)-1, -1, -1):
    if (lista[i]<=30):
        del lista[i]
print(lista)
