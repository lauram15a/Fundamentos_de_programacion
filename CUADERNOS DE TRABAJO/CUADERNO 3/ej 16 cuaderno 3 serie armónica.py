#LAURA MAMBRILLA MORENO
#EJ 16 CUADERNO 3

"""
. Escribe un programa que pida un número límite y calcule cuántos términos de la
serie armónica son necesarios para que su suma supere dicho límite. Es decir,
dado un límite introducido por el usuario (por ejemplo 50) se trata de determinar
el menor número n tal que:
1 + 1/2 + 1/3 + 1/n > limite
En nuestro ejemplo, para un límite = 5, n sería 83. El programa ha de ser
robusto, es decir, ha de controlar que el número introducido por el usuario es un
entero positivo.
"""

def validacion_entero(entero):
    """
    float --> bool
    OBJ: Validar si el dato introducido por el usuario es un número entero
    """
    try:
        dato = int(entero)
        if entero > 0:
            validacion = True
        else:
            validacion = False
    except:
        print ('El dato introducido no es entero.')
        validacion = False
    return validacion

def leer_entero_validado():
    """
    nada --> int
    OBJ: Solicita un entero al usuario, lo valida y lo retorna sólo cuando se ha asegurado de que es realmente un entero
    """
    entero = int(input('Introduzca un número entero: '))
    valido_entero = validacion_entero(entero)
    while valido_entero == False:
        entero = input('Introduzca un número entero positivo: ')
        valido_entero = validacion_entero(entero)
    return entero


def terminos (entero):
    """
    int --> int
    OBJ: pedir un número límite y calcule cuántos términos de la serie armónica son necesarios para que su suma supere dicho límite.
    """
    vueltas = 0 #vueltas = i
    suma = 0
    while suma < entero:
        vueltas = vueltas + 1
        suma = suma + 1/vueltas
    return vueltas

#main
entero = leer_entero_validado()
print ('Son necesarios ', terminos (entero), 'términos para completar la serie armónica')
