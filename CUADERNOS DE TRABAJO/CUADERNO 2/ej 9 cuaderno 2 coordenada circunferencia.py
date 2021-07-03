

#Ejercicio 9
#Escribe una función que determine si un punto de coordenadas en 2D está o no sobre la circunferencia x2+y2=1000.


print ('Escriba una coordenada para comprobar si pertenece a la circunferencia x**2 + y**2 = 1000:')
x = float (input('x = '))
y = float (input('y = '))

print ('¿Pertenece a la circunferencia?')

def circunferencia (x,y):
    """
    float, float --> booleano
    OBJ: determinar si la coordenada se encuentra sobre la circunferencia x**2 + y**2 = 1000
    """
    suma_coordenada = x**2 + y**2
    return suma_coordenada <= 1000


print (circunferencia (x,y))

      
