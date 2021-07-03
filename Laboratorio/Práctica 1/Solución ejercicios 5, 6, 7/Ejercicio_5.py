'''
Cuaderno de trabajo 1.pdf - Ejercicio 5:

Descripción: Calcular segundos desde y hasta medianoche
'''

#Programa principal
hora = int(input('Introduzca las horas: '))
minutos = int(input('Introduzca los minutos: '))
segundos = int(input('Introduzca los segundos: '))

print('Hora introducida: %d:%d:%d'%(hora,minutos,segundos))

seg_desde = (hora * 3600) + (minutos * 60) + segundos
seg_hasta = (24 * 3600) - seg_desde

print('\nHan pasado %d segundos desde medianoche.'%(seg_desde))
print('Quedan %d segundos hasta la siguiente medianoche.'%(seg_hasta))
