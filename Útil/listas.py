#Crear lista
lista = [10, 20, 30, 40]
print(lista)

#Crear lista de 10 elementos con el valor 0
#Forma 1
lista = [0] * 10
#Forma 2
lista = []
for i in range(10):
    lista.append(0)
print(lista)

#Acceder a un elemento
lista = [10, 20, 30, 40]
print(lista[2])

#Cambiar el valor de un elemento
lista[2] = 25

#Recorrer lista donde i toma cada valor
for i in lista: 
    print(i)
    
#Recorrer lista donde i es el índice
for i in range(len(lista)):
    print(i, lista[i])

#Concatenar listas
lista = lista + [50]
print(lista)

#Igualar listas
lista2 = lista
lista[0] = 1
print(lista)
print(lista2)

#Subrango
lista2 = lista[0:2]
print(lista2)

#Copiar lista
lista2 = lista[:]
lista[0] = 10
print(lista)
print(lista2)

#Recorrer lista al revés
for i in range(len(lista)-1, -1, -1):
    print(i, lista[i])
for i in reversed(range(len(lista))):
    print(i, lista[i])

#Eliminar un valor
del lista[0]
print(lista)

#Eliminar valores menores o iguales que 30
for i in range(len(lista)-1, -1, -1):
    if (lista[i]<=30):
        del lista[i]
print(lista)

#ordenar alfabéticamente (primero ordena mayúsculas y después minúsculas)
frutas = ['pera', 'paraguayo', 'fresa', 'plátano', 'Manzana', 'Aguacate']
frutas.sort()
print(frutas)
