#Método de ordenación por selección

def ordenacion_por_seleccion(lista):
    for i in range(len(lista)-1,0,-1):
        posicion = 0
        for j in range(1,i+1):
            if lista[j]>lista[posicion]:
                posicion = j

        temp = lista[i]
        lista[i] = lista[posicion]
        lista[posicion] = temp
    print (lista)

lista = [54,26,93,17,77,31,44,55,20]
ordenacion_por_seleccion(lista)
