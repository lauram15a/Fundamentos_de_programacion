#Laura Mambrilla Moreno
#Ej 18 cuaderno 5

"""
Programar una función que reciba un diccionario y una lista y que como
salida genere dos listas:
a. una lista con todos los valores de aquellos elementos de la lista que
están en el diccionario,
b. otra lista con los valores de los elementos que NO están en el
diccionario.
"""

def lista_dicionario (diccionario, lista):
    """
    list, dic --> list
    OBJ: crear lista con los elementos que estén en el diccionario
    """
    lista_si = []
    lista_no = []
    for i in range (len(lista)):
        if lista[i] in diccionario.keys():
            lista_si.append(diccionario[lista[i]])
            #elimino los elementos del diccionario nuevo que están en la lista
            if i == 0:
                dic_nuevo = diccionario.copy() #hago copia del diccionario
            del dic_nuevo[lista[i]]
    for v in dic_nuevo.values(): #solo recorre los valores
        lista_no.append(v)
    return lista_si, lista_no
                                        
    
#main
diccionario = {'a':'Buenos días', 1:15, 'bhj': 'casi', ('hola', 'que', 'tal'):'Bien, gracias', 'b':62}
lista =['a', ('hola','que','tal'), 564, 1, 'Aranda']

print(diccionario)
print(lista)
print('')
print(lista_dicionario (diccionario, lista))
