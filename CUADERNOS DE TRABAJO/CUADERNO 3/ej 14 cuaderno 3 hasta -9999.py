#LAURA MAMBRILLA MORENO
#Ejercicio 14 - Cuaderno 3

"""
Escribe un programa que lea una serie de números enteros hasta que se
introduzca el número -9999, y cuente el total de números introducidos, el total de
valores positivos y el total de valores negativos (no consideres el cero ni positivo
ni negativo). Reutilizar la función del ejercicio 9 para validar tus entradas.
"""

def validacion_entero(entero):
    """
    float --> bool
    OBJ: Validar si el dato introducido por el usuario es un número entero
    """
    try:
        dato = int(entero)
        validacion = True
    except:
        print ('El dato introducido no es entero.')
        validacion = False
    return validacion

def leer_entero_validado():
    """
    nada --> int
    OBJ: Solicita un entero al usuario, lo valida y lo retorna sólo cuando se ha asegurado de que es realmente un entero
    """
    entero = input('Introduzca un número entero: ')
    valido_entero = validacion_entero(entero)
    while valido_entero == False:
        entero = input('Introduzca un número entero: ')
        valido_entero = validacion_entero(entero)
    return entero

def total():
    """
    int --> int
    OBJ: introducir números hasta que se intro. -9999 y contar los nº positivos y negativos
    """
    intentos = 1
    cont_positivos = 0
    cont_negativos = 0
    cont_ceros = 0
    entero = int(leer_entero_validado())
    while entero != -9999:
        intentos = intentos + 1 
        if entero < 0:
            cont_negativos = cont_negativos + 1
        elif entero > 0:
            cont_positivos = cont_positivos + 1
        else:
            cont_ceros = cont_ceros + 1
        entero =int(leer_entero_validado())
    print ('')
    print('Intentos totales: ',intentos)
    print('Total números positivos: ',cont_positivos)
    print('Total números negativos: ',cont_negativos + 1)
    print('Total ceros: ', cont_ceros)


#main
total()
