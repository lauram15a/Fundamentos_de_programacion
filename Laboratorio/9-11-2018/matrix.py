#Funciones
def crea_matrix(rows, cols):
    matrix = [0] * rows
    for i in range(rows):
        matrix[i] = [0] * cols
    return matrix

def crea_matrix2(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(0)
    return matrix

def imprime_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("%d "%(matrix[i][j]), end="")
        print()

#Programa Principal
filas = 3
columnas = 3
matriz = crea_matrix(filas,columnas)
matriz[1][1] = 5
print(matriz)
imprime_matrix(matriz)
