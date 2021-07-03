#ej 3

#funciones
def ordenar_alfabéticamente(lista):
    """
    """
    lista_ordenar = []
    for i in range (len(lista)):
        for j in range (len(i)):
            lista_ordenar.append(lista[i][j])
    lista_ordenar.sort()
    for i in range (len(lista_ordenar)):
        for j in range (len(lista)):
            if lista_ordenar[i] == lista[j]:
                lista[i] == lista[j]
    return lista
                
                

    
#main
lista = ['Hola que tal','como estas','muy bien gracias']
print (ordenar_alfabéticamente(lista))
