#Laura Mambrilla Moreno
#Ej 4 cuaderno 5

"""
Implementa una estructura Punto2D con dos coordenadas x e y. Programa
después funciones para su suma y resta.
"""

class Punto2D :
    def __init__ (self, x, y):
        self.x = x
        self.y = y

def crear_punto ():
    """
    nada --> float, float
    OBJ: crear punto
    """
    x = float(input('\nx = '))
    y = float(input('y = '))
    punto = Punto2D(x, y)
    return punto

def suma_resta (num_puntos, lista_puntos):
    """
    float, float --> float
    OBJ: sumar y restar puntos
    """
    x_suma = 0
    y_suma = 0

    x_resta = 0
    y_resta = 0

    #crear punto
    for i in range (num_puntos):        
        punto = crear_punto()
        lista_puntos.append(punto)
    #suma
    for i in range (len(lista_puntos)):
        x_suma += lista_puntos[i].x
        y_suma += lista_puntos[i].y
    suma_puntos = Punto2D (x_suma,y_suma)
    #resta
    for i in range (len(lista_puntos)):
        x_resta -= lista_puntos[i].x
        y_resta -= lista_puntos[i].y
        if i == 0:
            x_resta= -1*x_resta
            y_resta = -1*y_resta
    resta_puntos = Punto2D (x_resta,y_resta)
    print ('\nSuma: (',suma_puntos.x,',' ,suma_puntos.y,')')
    print ('Resta: (',resta_puntos.x,',', resta_puntos.y,')')


#main
num_puntos = int(input('\n¿Con cuántos puntos quieres operar?: '))
lista_puntos = []
suma_resta (num_puntos, lista_puntos)
                 
