#Funciones
def validar_entero(strInt):
    ''' str -> bool
    OBJ: Valida si la cadena de texto es un entero'''
    try:
        int(strInt)
        esEntero = True
    except ValueError:
        esEntero = False
    return esEntero

#Programa principal
cadena = input("Introduce una cadena: ")
print("Es entero: %s"%(validar_entero(cadena)))
