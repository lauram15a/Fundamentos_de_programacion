#LAURA MAMBRILLA MORENO
#EJERCICIO 11 CUADERNO 3

"""
Programa una función que permita determinar si un determinado carácter es una
vocal o no, utilizando la construcción “if-elif”. Repite el ejercicio utilizando esta
vez el operador booleano OR y observa las diferencias.
"""

#IF-ELIF

def vocal_if(vocal):
    """
    str --> bool
    OBJ: determinar si un caracter es una vocal o no
    """
    if vocal=='a':
        return True
    elif vocal=='A':
        return True
    elif vocal=='e':
        return True
    elif vocal=='E':
        return True
    elif vocal=='i':
        return True
    elif vocal=='I':
        return True
    elif vocal=='o':
        return True
    elif vocal=='O':
        return True
    elif vocal=='u':
        return True
    elif vocal=='U':
        return True
    else:
        return False
    if True:
        print (vocal, ' es una vocal')
    else:
        print (vocal, ' NO es una vocal')

#main
vocal=str(input('Introduce una vocal: '))
print('¿Es "',vocal,'" una vocal?')
print(vocal_if(vocal))
