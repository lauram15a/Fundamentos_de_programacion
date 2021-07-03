#Descripción: Paso de parametros (datos inmutables).

#Funciones
def area_rectangulo(altura, anchura):
    """ float --> float
    OBJ: Calcula el area de un rectangulo
    PRE: altura>=0, ancho>=0 """
    altura = 10
    return altura*anchura

#Programa principal
altura = 5
anchura = 5
area = area_rectangulo(altura, anchura)
print('%d' %altura)
print('%d' %area)
