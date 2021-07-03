#LAURA MAMBRILLA MORENO
#EJ 10 CUADERNO 3

""""
Codifica un subprograma que reciba un número entero, y si es entre 1 y 12
escriba un mensaje por pantalla indicando el mes a que dicho número
corresponde. En caso contrario deberá mostrar un mensaje de error. Valida las
entradas utilizando la función del ejercicio 9.
"""

def validacion_entero(entero):
    """float -> bool
       OBJ: Validar si el dato introducido por el usuario es un numero entero"""
    try:
        elem = int(entero)
        validacion = True
    except:
        print("El dato introducido no es un numero entero.")
        validacion = False
    return validacion

def leer_entero_validado():
    """nada -> int
       OBJ: Solicita un entero al usuario, lo valida y lo retorna sólo cuando se ha asegurado de que es realmente un entero
    """
    entero = input("Introduzca un numero entero: ")
    valido_entero = validacion_entero(entero)
    while valido_entero == False:
        entero = input("Introduzca un numero entero: ")
        valido_entero = validacion_entero(entero)
    return entero

entero = leer_entero_validado()

if entero == '1' :
    print('El mes es Enero')
elif entero == '2' :
    print ('El mes es Febrero')
elif entero == '3' :
    print ('El mes es Marzo')
elif entero == '4' :
    print ('El mes es Abril')
elif entero == '5' :
    print ('El mes es Mayo')
elif entero == '6' :
    print ('El mes es Junio')
elif entero == '7' :
    print ('El mes es Julio')
elif entero == '8' :
    print ('El mes es Agosto')
elif entero == '9' :
    print ('El mes es Septiembre')
elif entero == '10' :
    print ('El mes es Octubre')
elif entero == '11' :
    print ('El mes es Noviembre')
elif entero == '12' :
    print ('El mes es Diciembre')
else:
    print ('Error, el entero introducido no corresponde a ningun mes')
