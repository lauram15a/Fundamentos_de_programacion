#Laura Mambrilla Moreno
#Ejercicio 1 Cuaderno 4

"""
Escribir una función que sume dos listas de igual longitud y retorne otra lista
que contenga la suma de las originales elemento a elemento.
"""

#funciones

def suma_listas (l_1, l_2):
    """
    list, list --> list
    OBJ: sumar l_1 + l_2
    """
    l_3 = []
    for i in range (len(l_1)):
        l_3.append (l_1[i] + l_2[i])
    return l_3
    

#main
l_1 = [1,2,3,4]
l_2 = [5,6,7,8]

if len(l_1) == len(l_2):
    print (l_1, '+', l_2, '=', suma_listas (l_1, l_2))
else:
    print ('Logitud de listas desigual.')
