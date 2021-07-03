#EJ 2.1

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




#EJ 2.2

#funciones
def trino (n):
    """
    int --> bool
    OBJ: num trino ¿sí o no?
    """
    if n // 100 <= 9:
        num_cifras =3      
    else:
        print ('No es un número de 3 cifras')
        return False
    """ #no sirve para este ejercicio
    if num_cifras <= 1 or num_cifras>3:
        return False
    if num_cifras == 2:
        unidades = n % 10
        decenas = ((n - unidades)/10) % 10
        if abs(decenas - unidades) == 3:
            return True
        else:
            return False
    """
    if num_cifras == 3:
        unidades = n % 10
        decenas = ((n - unidades)/10) % 10
        centenas = ((n - decenas*10-unidades)/100) % 100
        if abs(centenas - decenas) == 3 and abs(decenas - unidades) == 3:
            return True
        else:
            return False        

def leer_num ():
    """
    nada --> int
    OBJ: sin n es trino, sumar los 3 nums impares siguientes a él
    """
    n = int (input('Número de 3 cifras: '))
    valido_trino = trino (n)
    while valido_trino == False:
        n = int(input('Introduzca un número trino de 3 cifras: '))
        valido_trino = trino(n)
    return n

def suma ():
    """
    int --> int
    OBJ: suma de los tres siguientes números impares de n
    """
    n = int (leer_num())
    i = 0
    if n % 2 == 0: #n es par
        n_1 = n + 1
        n_2 = n + 3
        n_3 = n + 5
        suma = n_1 + n_2 + n_3
        print ('Acaba de introducir un número trino. Su valor es ',n,'\nSuma de los 3 impares siguientes: ',n_1,'+',n_2,'+',n_3,'=',suma)
    else:
        n_1 = n + 2
        n_2 = n + 4
        n_3 = n + 6
        suma = n_1 + n_2 + n_3
        print ('Acaba de introducir un número trino. Su valor es ',n,'\nSuma de los 3 impares siguientes: ',n_1,'+',n_2,'+',n_3,'=',suma)
     
        

#main

suma()
