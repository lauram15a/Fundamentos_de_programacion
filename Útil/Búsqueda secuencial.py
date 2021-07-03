#Búsqueda secuencial

def busqueda_secuencial(lista, item):
    i = 0
    posicion = -1
    while (i<len(lista) and posicion<0):
        if (lista[i] == item):
            posicion = i
        i +=1
    return posicion
