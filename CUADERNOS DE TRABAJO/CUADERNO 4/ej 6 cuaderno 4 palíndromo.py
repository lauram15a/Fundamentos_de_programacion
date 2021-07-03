#LAURA MAMBRILLA MORENO
# EJ 6 CUADERNO 4

"""
Implementar una función que compruebe si una palabra es un palíndromo.
"""


#funciones
def palindromo (palabra):
    """
    str --> bool
    OBJ: palíndromo o no
    """
    lista = list(palabra) #decompongo la palabra
    long = len(lista)
    palin = True #inicializo palin(dromo)
    i= -1
    #num impar de letras
    if long%2 != 0 :
        while i < (long-1)/2 and palin != False: #mientras la posi sea menor que la mitad del num de elementos
            i = i+ 1
            j = long - 1 - i
            if lista[i] == lista[j]:
                palin = True
            else:
                palin = False
    #num par de letras
    else:
        while i < (long/2) and palin != False:
            i = i+ 1
            j = long - i - 1
            if lista[i] == lista[j]:
                palin = True
            else:
                palin = False
    return palin
            

#main
palabra = str(input('Escribe una palabra: '))
print('\n¿"',palabra,'" es palíndromo?')
print(palindromo(palabra))
