#Laura Mambrilla Moreno
#ej 13 cuaderno 5

"""
Realice una aplicación que permita sumar dos matrices de tamaño 3x4. Las
matrices contienen datos sobre Puntos2D y que realice las siguientes tareas:
a. Solicitar datos para la matriz A.
b. Solicitar datos para la matriz B.
c. Presente el resultado de matriz A + matriz B.
"""

class Punto2D :
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        

def crear_matriz(num_filas, num_columnas):
    """
    nada --> matrix
    OBJ: crear matriz
    """
    matriz = []
    for i in range (num_filas):
        matriz.append([0]*num_columnas)
    #rellenar la matriz
    for i in range (num_filas):
        for j in range (num_columnas):
            punto = crear_punto()
            matriz [i][j] = punto
    return matriz


def crear_matriz_ceros(num_filas, num_columnas):
    """
    nada --> matrix
    OBJ: crear matriz
    """
    matriz = []
    for i in range (num_filas):
        matriz.append([0]*num_columnas)
    for i in range (num_filas):
        for j in range (num_columnas):
            x = 0
            y = 0
            punto = Punto2D(x, y)
            matriz [i][j] = punto
    return matriz


def crear_punto ():
    """
    """
    x = float(input('\nx = '))
    y = float(input('y = '))
    punto = Punto2D(x, y)
    return punto


def suma_puntos (A, B, C):
    """
    matrix, matrix --> matrix
    OBJ: sumar matrices cuyos elementos son puntos
    """
    for i in range (num_filas):
        for j in range (num_columnas):
            punto_A = A[i][j]
            punto_B = B[i][j]
            punto_C = C[i][j]
            
            punto_C.x = punto_A.x + punto_B.x
            punto_C.y = punto_A.y + punto_B.y

            C[i][j] = punto_C.x, punto_C.y
    return C


#main
num_filas = 3
num_columnas = 4
print('\nmatriz A')
A = crear_matriz(num_filas, num_columnas)
print('\nmatriz B')
B = crear_matriz(num_filas, num_columnas)
print('\nmatriz C (A+B)')
C = crear_matriz_ceros(num_filas, num_columnas)
print('')
print(suma_puntos (A, B, C))
