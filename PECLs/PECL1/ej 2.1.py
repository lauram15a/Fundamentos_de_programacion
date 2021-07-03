#ej 2

#funciones
def trino (num_cifras, n):
    """
    int --> bool
    OBJ: num trino ¿sí o no?
    """
    if num_cifras <= 1 or num_cifras>3:
        return False
    if num_cifras == 2:
        unidades = n % 10
        decenas = ((n - unidades)/10) % 10
        if abs(decenas - unidades) == 3:
            return True
        else:
            return False
    if num_cifras == 3:
        unidades = n % 10
        decenas = ((n - unidades)/10) % 10
        centenas = ((n - decenas*10-unidades)/100) % 100
        if abs(centenas - decenas) == 3 and abs(decenas - unidades) == 3:
            return True
        else:
            return False
    

#main
num_cifras = int ( input('¿Cuántas cifras tiene el número que vas a meter? Como muccho pueden ser 3:'))
n = int (input('Número: '))
print('\n¿Es trino?')
print(trino (num_cifras, n))
