#LAURA MAMBRILLA MORENO
#Ej 3 Cuaderno 7

"""
Modifique el programa anterior para que ordene el array en función del
número de palabras que hay en la frase. Use ahora el método de selección.
Pista: utiliza split()
"""

#funciones

def mayor_num_palabras(frase1, frase2):
    """
    """
    lista_frase1 = frase1.split(' ')
    lista_frase2 = frase2.split(' ')
        
    return len(lista_frase1) > len(lista_frase2)

def ordenacion_por_seleccion(lista):
    for i in range(len(lista)-1,0,-1):
        posicion = 0
        for j in range(1,i+1):
            if mayor_num_palabras(lista[j], lista[posicion]):
                posicion = j

        temp = lista[i]
        lista[i] = lista[posicion]
        lista[posicion] = temp
    print (lista)

def imprimir_lista (lista):
    """
    """
    print('')
    for i in lista:
        print (i)
        

#main
lista = ['fha iaueslfh udhsfa','ehf qipuefhuqewñqe few','eñkjdf qoewifh qñfroq4 yre','laduk iwDHIUWEAD F','uisdycbwuefgqi','efyrb aeq geq xhwashd bweo dwf','heqgf eygfui qf jd f','ufh eruqf iuhdjfhvw ori ekcf','uqefy udwfn jcn','djfh qeruifh iuqe f']

"""
lista = []
for i in range (10):
    frase = str(input('-->'))
    lista.append(frase)
"""
ordenacion_por_seleccion(lista)
imprimir_lista (lista)
