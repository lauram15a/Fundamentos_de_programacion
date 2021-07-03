#Registros (mediante class)

#Librerias
import copy

#Tipos
class tPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class tTriangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

#Funciones
def copyTriangle(t):
    p1 = tPoint(t.point1.x, t.point1.y)
    p2 = tPoint(t.point2.x, t.point2.y)
    p3 = tPoint(t.point3.x, t.point3.y)
    return tTriangle(p1, p2, p3)
def printTriangle(t):
    str1 = "point1=tPoint(x="+str(t.point1.x)+", y="+str(t.point1.y)+")"
    str2 = "point2=tPoint(x="+str(t.point2.x)+", y="+str(t.point2.x)+")"
    str3 = "point3=tPoint(x="+str(t.point3.x)+", y="+str(t.point3.x)+")"
    output = "tTriangle("+str1+", "+str2+", "+str3+")"
    print(output)

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
printTriangle(triangle)
printTriangle(triangle2)
printTriangle(triangle3)
printTriangle(triangle4)
printTriangle(triangle5)

lista = [triangle, triangle5]
for i in range(len(lista)):
    lista[i].point3.x = 50.0
print(lista)
