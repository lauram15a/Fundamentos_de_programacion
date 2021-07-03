#LAURA MAMBRILLA MORENO
#Ej 2 Cuaderno 7

"""
Realice un programa que almacene 10 frases diferentes en un array y nos
permita ordenar el array descendentemente por la longitud de la cadena
usando el método de inserción.
"""

#funciones

def mayor(frase1, frase2):
    """
    """
    return len(frase1) > len(frase2)

"""
def ordenacion_por_insercion (lista):
    n = len(lista)
    for i in range(n):
        j = i-1
        val = lista[i]
        while j>0 and len(val)>len(lista[j]): #se cambia el mayor del val para poner ascendente o descendente
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = val
"""

def ordenacion_por_insercion (lista):
  for i in range(1,len(lista)) :
    aux=lista[i]
    j=i
    while j>0 and mayor(aux,lista[j-1]) :
      lista[j]=lista[j-1]
      j-=1
    lista[j]=aux

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
ordenacion_por_insercion (lista)
imprimir_lista (lista)
