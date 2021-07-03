#Laura Mambrilla Moreno
#Ejercicio 2 Cuaderno 4

"""
Modifique el ejercicio anterior permitiendo que las listas sean desiguales. Los
elementos sobrantes de la lista más larga se añadirán al final de la lista
resultante.

"""

#funciones

def suma_listas (lista1, lista2):
    """
    list, list --> list
    OBJ: sumar l_1 + l_2
    """
    lista3= []
    #lista1 MAYOR  
    if len(lista1) > len(lista2):
        lista2nueva = lista2[:] #copio lista2 
        for j in range(len(lista1)-len(lista2)):
            lista2nueva.append(0) #modifico la nueva lista2, igualando su len a la de lista1
        for i in range (len(lista1)):
            lista3.append(lista1[i] + lista2nueva[i])
    #lista2 MAYOR
    elif len(lista1) < len(lista2):
        lista1nueva = lista1[:] #copio lista1
        for j in range(len(lista2)-len(lista1)):
            lista1nueva.append(0) #modifico la nueva lista1, igualando su len a la de lista2
        for i in range (len(lista2)):
            lista3.append(lista1nueva[i] + lista2[i])
    #IGUALES
    else:
        for i in range (len(lista1)):
            lista3.append(lista1[i] + lista2[i])
    return lista3
    
    

#main
lista1 = [1,2,3,4,5]
lista2 = [70,80,90,0,5]

print (lista1,'+',lista2,'=',suma_listas(lista1, lista2))
