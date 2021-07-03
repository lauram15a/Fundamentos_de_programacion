#Laura Mambrilla Moreno
#ej 15 cuaderno 5

"""
Realice una aplicación que permita comprobar si un tablero de Conecta4
(https://es.wikipedia.org/wiki/Conecta_4) ha completado las 4 en raya. La
aplicación deberá:
a. Solicitar datos para un tablero de 7x6
b. Solicitar introducir valores para representar las fichas del tablero en
un momento concreto del juego
c. Mostrar por pantalla el tablero con los valores introducidos
d. Indicar si alguna fila, columna o diagonal incluye 4 en raya (4 casillas
consecutivas con una ficha de igual color).
"""

class Casilla:
    def __init__ (self, hay_ficha, color):
        self.hay_ficha = hay_ficha
        self.color = color

def crear_tablero (num_filas, num_columnas):
    """
    nada --> matrix
    OBJ: crear matriz
    """
    tablero = []
    for i in range (num_filas):
        tablero.append(['-']*num_columnas)
    return tablero

def tirada ():
    """
    """
    tablero = crear_tablero (num_filas, num_columnas)
    jugador = 1
    cuatro_en_raya = False
    print('')
    print (' ',0, 1, 2, 3, 4, 5)
    print (0, tablero[0][0], tablero[0][1], tablero[0][2], tablero[0][3], tablero[0][4], tablero[0][5])
    print (1, tablero[1][0], tablero[1][1], tablero[1][2], tablero[1][3], tablero[1][4], tablero[1][5])
    print (2, tablero[2][0], tablero[2][1], tablero[2][2], tablero[2][3], tablero[2][4], tablero[2][5])
    print (3, tablero[3][0], tablero[3][1], tablero[3][2], tablero[3][3], tablero[3][4], tablero[3][5])
    print (4, tablero[4][0], tablero[4][1], tablero[4][2], tablero[4][3], tablero[4][4], tablero[4][5])
    print (5, tablero[5][0], tablero[5][1], tablero[5][2], tablero[5][3], tablero[5][4], tablero[5][5])
    print (6, tablero[6][0], tablero[6][1], tablero[6][2], tablero[6][3], tablero[6][4], tablero[6][5])
    while cuatro_en_raya != True:
        if jugador == 1:
            print ('\nJUGADOR 1 --> O')
        else:
            print ('\nJUGADOR 2 --> X')

        fila = int(input('\nFila: '))
        columna = int(input('Columna: '))

        if 0 <= fila <= 6 and 0 <= columna <= 5:
            if tablero[fila][columna] == '-' :
                if jugador == 1:
                    ficha = 'O'
                    color = 'rojo'
                else:
                    ficha = 'X'
                    color = 'amarillo'
                tablero[fila][columna] = ficha
                hay_ficha = False
            else:
                print('Casilla ocupada. Pierdes el turno.')
                hay_ficha = True
            casilla = tablero[fila][columna]
            casilla = Casilla(hay_ficha, color)          

            #vertical
            if tablero[0][columna] == ficha and tablero[1][columna] == ficha and tablero[2][columna]== ficha and tablero[3][columna] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA VERTICAL!!!!')
            if tablero[4][columna] == ficha and tablero[1][columna] == ficha and tablero[2][columna] == ficha and tablero[3][columna] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA VERTICAL!!!!')
            if tablero[4][columna] == ficha and tablero[5][columna] == ficha and tablero[2][columna] == ficha and tablero[3][columna] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA VERTICAL!!!!')
            if tablero[4][columna] == ficha and tablero[5][columna] == ficha and tablero[6][columna] == ficha and tablero[3][columna] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA VERTICAL!!!!')

            #horizontal
            if tablero[fila][0] == ficha and tablero[fila][1] == ficha and tablero[fila][2] == ficha and tablero[fila][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA HORIZONTAL!!!!')
            if tablero[fila][4] == ficha and tablero[fila][1] == ficha and tablero[fila][2] == ficha and tablero[fila][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA HORIZONTAL!!!!')
            if tablero[fila][4] == ficha and tablero[fila][5] == ficha and tablero[fila][2] == ficha and tablero[fila][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA HORIZONTAL!!!!')

            #diagonal
                #naranja
            if tablero[3][0] == ficha and tablero[2][1] == ficha and tablero[1][2] == ficha and tablero[0][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
                #verde
            if tablero[4][0] == ficha and tablero[3][1] == ficha and tablero[2][2] == ficha and tablero[1][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[0][4] == ficha and tablero[3][1] == ficha and tablero[2][2] == ficha and tablero[1][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
                #azul
            if tablero[5][0] == ficha and tablero[4][1] == ficha and tablero[3][2] == ficha and tablero[2][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[1][4] == ficha and tablero[4][1] == ficha and tablero[3][2] == ficha and tablero[2][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[1][4] == ficha and tablero[0][5] == ficha and tablero[3][2] == ficha and tablero[2][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
                #morado
            if tablero[5][1] == ficha and tablero[4][2] == ficha and tablero[3][3] == ficha and tablero[2][4] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[1][5] == ficha and tablero[4][2] == ficha and tablero[3][3] == ficha and tablero[2][4] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[5][1] == ficha and tablero[4][2] == ficha and tablero[3][3] == ficha and tablero[6][0] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
                #rosa
            if tablero[5][2] == ficha and tablero[4][3] == ficha and tablero[3][4] == ficha and tablero[2][5] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[5][2] == ficha and tablero[4][3] == ficha and tablero[3][4] == ficha and tablero[6][1] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
                #amarillo
            if tablero[6][2] == ficha and tablero[5][3] == ficha and tablero[4][4] == ficha and tablero[3][5] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            #al revés
                #naranja
            if tablero[0][2] == ficha and tablero[1][3] == ficha and tablero[2][4] == ficha and tablero[3][5] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')   
                #verde
            if tablero[0][1] == ficha and tablero[1][2] == ficha and tablero[2][3] == ficha and tablero[3][4] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[4][5] == ficha and tablero[1][2] == ficha and tablero[2][3] == ficha and tablero[3][4] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
                #azul
            if tablero[0][0] == ficha and tablero[1][1] == ficha and tablero[2][2] == ficha and tablero[3][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[4][4] == ficha and tablero[1][1] == ficha and tablero[2][2] == ficha and tablero[3][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[4][4] == ficha and tablero[5][5] == ficha and tablero[2][2] == ficha and tablero[3][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
                #morado
            if tablero[3][0] == ficha and tablero[4][1] == ficha and tablero[5][2] == ficha and tablero[6][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
                #rosa
            if tablero[1][0] == ficha and tablero[2][1] == ficha and tablero[3][2] == ficha and tablero[4][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[5][4] == ficha and tablero[2][1] == ficha and tablero[3][2] == ficha and tablero[4][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[5][4] == ficha and tablero[6][5] == ficha and tablero[3][2] == ficha and tablero[4][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
                #amarillo
            if tablero[2][0] == ficha and tablero[3][1] == ficha and tablero[4][2] == ficha and tablero[5][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')
            if tablero[6][4] == ficha and tablero[3][1] == ficha and tablero[4][2] == ficha and tablero[5][3] == ficha:
                cuatro_en_raya = True
                print ('\n¡¡¡¡ 4 EN RAYA DIAGONAL!!!!')

        else:
            print('Casilla fuera de rango. Pierdes el turno.')
            
        print('')
        print (' ',0, 1, 2, 3, 4, 5)
        print (0, tablero[0][0], tablero[0][1], tablero[0][2], tablero[0][3], tablero[0][4], tablero[0][5])
        print (1, tablero[1][0], tablero[1][1], tablero[1][2], tablero[1][3], tablero[1][4], tablero[1][5])
        print (2, tablero[2][0], tablero[2][1], tablero[2][2], tablero[2][3], tablero[2][4], tablero[2][5])
        print (3, tablero[3][0], tablero[3][1], tablero[3][2], tablero[3][3], tablero[3][4], tablero[3][5])
        print (4, tablero[4][0], tablero[4][1], tablero[4][2], tablero[4][3], tablero[4][4], tablero[4][5])
        print (5, tablero[5][0], tablero[5][1], tablero[5][2], tablero[5][3], tablero[5][4], tablero[5][5])
        print (6, tablero[6][0], tablero[6][1], tablero[6][2], tablero[6][3], tablero[6][4], tablero[6][5])

                
        jugador = jugador * (-1)


#main
print ('\n4 EN RAYA')
print('\n Filas --> [0,6] \n Columnas --> [0,5]')


num_filas = 7
num_columnas = 6

tirada ()
