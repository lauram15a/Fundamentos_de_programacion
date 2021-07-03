#LAURA MAMBRILLA MORENO
#EJ 9 CUADERNO 3

"""
Ya has visto que la validación de entradas es algo tan presente que no podemos
huir de ello, así que si te parece vamos a escribir una función que solicite al
usuario introducir un entero y que no pare de pedírselo hasta que la información 
introducida sea válida. La idea es usar la construcción while combinada con las
funciones de validación programadas en el ejercicio 4, consiguiendo una función
cuya cabecera sería la siguiente:
def leer_entero_validado():
 ''' nada --> int
 OBJ: Solicita un entero al usuario, lo valida y lo retorna sólo
 cuando se ha asegurado de que es realmente un entero
 '''
Ahora te toca a ti completarla, codificando sus instrucciones. ¡Adelante!

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

#main
entero = int(leer_entero_validado())
print(entero, 'es un número entero')

