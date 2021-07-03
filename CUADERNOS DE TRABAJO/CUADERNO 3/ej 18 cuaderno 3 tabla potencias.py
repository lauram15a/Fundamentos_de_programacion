#Laura Mambrilla Moreno
#EJERCICIO 18

"""
Escribe un programa que lea un entero positivo n y genere:
   a. una tabla con las n primeras potencias de 2.
   b. una tabla con las potencias de 2 que son menores o iguales que n.

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

def tabla_primeras_potencias (entero):
    """
    int --> int
    OBJ: devolver una tabla con las n primeras potencias de 2.
    """
    for i in range (entero + 1):
        potencias_primeras = 2**i
        print ('2 ** ', i, '= ', potencias_primeras)

def tabla_menores_potencias (entero):
    """
    int --> int
    OBJ: devolver una tabla con las potencias de 2 que son menores o iguales que n.
    """
    if entero == 0:
        print ('-')
    elif entero == 1:
        print('2 ** 0 = 1')        
    else:
        print ('2 ** 0 = 1')
        potencias_menores = 0
        i = 1
        while potencias_menores < entero:
            i = i + 1
            if entero**(1/i) == 2:  # ej:  2**3=8  ; 8**(1/3)=2
                potencias_menores = 2**i
                print ('2 ** ', i-1, '= ', 2**(i-1))
                print ('2 ** ', i, '= ', potencias_menores)
            else:
                potencias_menores = 2**i
                print ('2 ** ', i-1 , '= ', 2**(i-1))
                            
              

#main
entero = int (leer_entero_validado())
print('\nTabla con las', entero,' primeras potencias de 2')
tabla_primeras_potencias (entero)
print ('\nTabla con las potencias de 2 que son menores o iguales que ',entero)
tabla_menores_potencias (entero)
