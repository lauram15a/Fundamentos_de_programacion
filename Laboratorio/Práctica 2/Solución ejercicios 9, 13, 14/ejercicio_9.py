'''
Cuaderno de trabajo 2.pdf - Ejercicio 9

Descripción: Calcular si un punto está sobre la circunferencia x^2+y^2=1000.
'''

#Funciones
def estaEnCircunferencia(x,y):
    '''float,float --> bool
    OBJ: Determina si x,y esta en la circunferencia x^2+y^2=1000'''
    res = x**2 + y**2 == 1000
    return res
    
#Programa principal
x = float(input("Introduce la coordenada x: "))
y = float(input("Introduce la coordenada y: "))

resultado = estaEnCircunferencia(x,y)

print(f'\nEl punto ({x},{y}) está en la circunferencia: {resultado}')
