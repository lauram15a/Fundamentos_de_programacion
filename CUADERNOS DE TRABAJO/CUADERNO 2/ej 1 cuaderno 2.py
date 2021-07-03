#Ejercicio 1 - Cuadreno 2

"""
Implementa una función “fuerza” que retorne el valor de la fuerza en función
de los valores de masa y aceleración recibidos como parámetros.
Implementa, posteriormente, un programa probador que, leyendo de
teclado los valores necesarios, invoque a la función “fuerza” y muestre por
pantalla el valor de la fuerza a partir de una masa y aceleración dadas.
"""

masa = float (input('Masa = '))
aceleracion = float (input('Acelación = '))

def fuerza (masa, aceleracion):
    """
    float, float --> float
    OBJ:
    """
    fuerza = masa * aceleracion
    return fuerza

print ('Fuerza = ',fuerza (masa, aceleracion))

print('')

#PROBADOR
print('Si masa=85 y aceleracion=62 --> ', fuerza(85,62))
