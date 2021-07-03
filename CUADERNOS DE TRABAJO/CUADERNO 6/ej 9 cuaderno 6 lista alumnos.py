#Laura Mambrilla Moreno
#Ej 9 Cuaderno 6

"""
Programar un algoritmo recursivo que obtenga la suma de las edades de todos
los elementos de una lista de alumnos. Un alumno está caracterizado por tres
atributos (nombre, edad, titulacion).
"""

class Alumno:
    def __init__ (self, nombre, edad, titulacion):
        self.nombre = nombre
        self.edad = edad
        self.titulacion = titulacion

def suma_edades (lista_alumnos):
    """
    """
    if len(lista_alumnos) == 1:
        return lista_alumnos[0].edad
    else:
        return lista_alumnos[0].edad + suma_edades(lista_alumnos[1::]) #así se elimina el primer elemento
    

#main
lista_alumnos = []
a1 = Alumno('Ana', 20, 'Farmacia')
a2 = Alumno('Mario', 16, 'CCAFYDE')
a3 = Alumno('Sonia', 23, 'Química')

lista_alumnos.append(a1)
lista_alumnos.append(a2)
lista_alumnos.append(a3)

print('\nLa suma de las edades de los alumnos es de: ',suma_edades (lista_alumnos))
