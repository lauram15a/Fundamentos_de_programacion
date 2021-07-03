#MÁQUINA TRAGAPERRAS

#librerías
import random
import sys

#funciones
def jugada (num_monedas):
    """
    int
    OBJ
    """
    while num_monedas != 0:
        num_monedas = num_monedas - 1
        num_1 = random.randrange(1,7)
        num_2 = random.randrange(1,7)
        num_3 = random.randrange(1,7)
        print ('\nTirada: ')
        print (num_1,',', num_2,',', num_3)
        
        #los 3 números distintos
        if num_1 != num_3 != num_2 and num_1 != num_2 != num_3 and num_3 != num_2 != num_1 : 
            num_monedas = num_monedas
            print ('No has ganado ninguna moneda')
        #Los 3 son iguales
        elif num_1 == num_2 == num_3: 
            num_monedas = num_monedas + 5
            print ('Has ganado 5 monedas')
        #hay 2 números iguales
        else: 
            num_monedas = num_monedas + 2
            print ('Has ganado 2 monedas')
            
        print('Le quedan', num_monedas, 'moneda(s).')
        seguir_jugando= str(input('\nENTER para seguir jugando.'))

        if seguir_jugando != "":
            print ('Has decidido dejar de jugar!!!!!!!')
            print ('\nHa acabado la partida con', num_monedas,' moneda(s).')
            num_monedas_final = num_monedas - num_monedas_inicio
            if num_monedas_final > 0:
                print('Has ganado', num_monedas_final,' moneda(s).')
            elif num_monedas_final < 0:
                print('Has perdido', (-1)*num_monedas_final,' moneda(s)')
            else:
                print ('No has ganado ninguna moneda.')
            sys.exit(-1)
          
    print ('\nTe has quedado sin monedas. \nFin de la partida.')
    return num_monedas

#main
print ('\nTRAGAPERRAS')
print ('\nEn cada tirada, se le cobrará una moneda.')
num_monedas=int(input('\nIntroduce el número de monedas con el que empieza a jugar:'))
num_monedas_inicio = num_monedas
print ('\nEmpieza la partida con ',num_monedas,' moneda(s).')

jugada(num_monedas)
