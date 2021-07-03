#ej 9 profe

def leer_entero_validado():
    """
    nada --> int
    OBJ: Solicita un entero al usuario y lo valida y lo retorna si solo si 
    """
    esValido = False
    while (not esValido):
        try:
            entero= int (input('introduce un entero'))
            esValido=True
        except ValueError:
            print ('El entero no es válido')
    return entero

#main
if __name__ == '__main__':
    entero= leer_entero_validado()
    print ('el entero es: ', entero)
