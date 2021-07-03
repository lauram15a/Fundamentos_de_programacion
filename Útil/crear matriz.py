#matriz

def crear_matriz():
    """
    nada --> matrix
    OBJ: crear matriz
    """
    #establecer la dimensión de la matriz
    num_filas = 3
    num_columnas = 4
    matriz = []
    for i in range (num_filas):
        matriz.append([0]*cum_columnas)
    #rellenar la matriz
    contador = 1
    for i in range (num_filas):
        for j in range (num_columnas):
            matriz [i][j] = contador
            contador += 1
    #imprimir la materiz en forma matemática
    for i in matriz:
        for j in i:
            print j, #la coma sirve para que se ponga inmediatamente a la derecha
        print #para que la siguiente fila se ponga abajo
            
