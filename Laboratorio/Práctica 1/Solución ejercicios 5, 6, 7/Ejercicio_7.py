'''
Cuaderno de trabajo 1.pdf - Ejercicio 7:

Descripción: Conversor de distancias
'''

#Programa principal
km = float(input('Introduzca una distancia (km): '))

m = km * 1000
dm = m / 10
hm = m / 100

print('\nDistancia en hectómetros: %.2f hm'%(hm))
print('Distancia en decámetros: %.2f dm'%(dm))
print('Distancia en metros: %.2f m'%(m))

