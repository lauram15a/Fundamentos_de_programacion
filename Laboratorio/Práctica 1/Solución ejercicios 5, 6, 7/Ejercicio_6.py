'''
Cuaderno de trabajo 1.pdf - Ejercicio 6:

Descripción: Contabilidad de camiones
'''

#Programa principal
distancia = float(input('Introduzca la distancia recorrida (km): '))
litros = float(input('Introduzca la cantidad de combustible usada (l): '))
precio = float(input('Introduzca el precio del combustible (€/l): '))
mantenimiento = float(input('Introduzca el coste de mantenimiento (€): '))

kmLitro = distancia / litros
costeTotal = (litros * precio) + mantenimiento
costeKm = costeTotal / distancia

print('\nKilómetros recorridos por litro: %.2f km/l'%(kmLitro))
print('Coste total del viaje: %.2f €'%(costeTotal))
print('Coste por kilómetro: %.2f €'%(costeKm))
