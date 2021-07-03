#Registros (mediante recordclass)

#Librerias
from recordclass import recordclass as Record
import copy

#Tipos
tPoint    = Record('tPoint', 'x y')
tTriangle = Record('tTriangle', 'point1 point2 point3')

#Funciones
def copyTriangle(t):
    p1 = tPoint(t.point1.x, t.point1.y)
    p2 = tPoint(t.point2.x, t.point2.y)
    p3 = tPoint(t.point3.x, t.point3.y)
    return tTriangle(p1, p2, p3)

#Programa principal
p1 = tPoint(0.0, 0.0)
p2 = tPoint(1.0, 0.0)
p3 = tPoint(0.0, 1.0)
triangle = tTriangle(p1, p2, p3)

triangle2 = triangle
triangle3 = copy.copy(triangle)
triangle4 = copy.deepcopy(triangle)
triangle5 = copyTriangle(triangle)

triangle.point1.x += 0.5
print(triangle)
print(triangle2)
print(triangle3)
print(triangle4)
print(triangle5)

lista = [triangle, triangle5]
for i in range(len(lista)):
    lista[i].point3.x = 50.0
print(lista)
