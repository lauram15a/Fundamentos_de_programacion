#ej 3

#librerías
import sys

#funciones

#a
def par_impar (coor):
    """
    int --> str
    OBJ: suma coordenadas par o impar
    """
    if coor % 2 == 0: #par
        print('Par')
    else:
        print('Impar')

#b
def dia_prin (x, y, dim):
    """
    int, int, int --> bool
    OBJ: si coordenada está en la diagonal principal
    """
    if dim%2 == 0: #dim par
        return 'No hay diagonal'
        dim = int(input('Introduzca dimendión impar si quiere comprobar o pulse "Enter" '))
        if dim == '':
            sys.exit(-1)
    pto_prin = (dim//2)+1
    if x == y and pto_prin == x:
        return True
    else:
        return False
            
#c
def dia_inversa (coor, dim):
    """
    int, int --> bool
    OBJ: dia inversa sí o no
    """
    if coor + 1 == dim:
        return True
    else:
        return False
 
    
#main común a apartados a, b, c
x= int(input('x= '))
y= int(input('y= '))
coor = x + y
dim = int(input('Dimensión tablero (nxn): '))
print(par_impar (coor))
print('¿Diago principal?',dia_prin (x, y, dim))
print('¿Diago inversa?',dia_inversa (coor, dim))

#APARTADO D

#funciones
def tablero (n):
    """
    int --> char
    OBJ: dibujar
    """
    for x in range (n):
        for y in range (n):
            while 
            if x==y:
                print('#', end='')
            if y==n-(n-1):
                print('$', end='')
                

#main d
n = int(input('n='))
tablero (n)
