#Laura Mambrilla Moreno
#Ej 5 cuaderno 7

"""
Haga un programa para gestionar las notas de una clase de 20 alumnos de
los cuales sabemos el nombre y la nota. El programa debe permitir:
a. Introducir los datos de los alumnos por teclado.
b. Dado un nombre de un alumno, buscarlo y modificar su nota,
mostrando el resultado por pantalla (empleando búsqueda secuencial).
c. Dado un nombre de un alumno, buscarlo y mostrar la información por
pantalla empleando búsqueda binaria.
d. Realizar la media de todas las notas.
e. Realizar la media de las notas superiores a 5.
f. Realizar la ordenación (método de selección) de los alumnos por notas
en orden descendente y mostrar la nota del alumno con mejor nota.
g. Utilizando el método de inserción, realizar la ordenación de los alumnos
por notas en orden ascendente y mostrar la nota del alumno que peor
nota haya sacado. 
"""

class Alumno :
    def __init__ (self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

#1
def introducir_datos (lista_alumnos):
    """
    """
    nombre = str(input('Nombre: '))
    nota = float (input('Edad: '))
    alumno = Alumno(nombre, nota)
    lista_alumnos.append(alumno)
    for i in range (len(lista_alumnos)):
        print('\nNombre: ',lista_alumnos[i].nombre,'\nNota: ',lista_alumnos[i].nota )

#2

def buscar_alumno (lista, nombre_alumno):
    """
    """
    i = 0
    posicion = -1
    while (i<len(lista) and posicion<0):
        if (lista[i].nombre == nombre_alumno):
            posicion = i
        i +=1
    return posicion

def modificar_nota (lista_alumnos):
    """
    """
    posicion = buscar_alumno (lista_alumnos, nombre_alumno)
    if posicion == -1:
        print('Alumno no encontrado')
    else:
        nota_nueva = float(input('Nueva nota: '))
        lista_alumnos[posicion].nota = nota_nueva
        print('\nNombre: ',lista_alumnos[posicion].nombre,'\nNota: ',lista_alumnos[posicion].nota )
        
#3
def busquedaBinaria(lista, nombre_alumno_binario):
    if len(lista) == 0:
        return False
    else:
        puntoMedio = len(lista)//2
        if lista[puntoMedio].nombre == nombre_alumno_binario:
            return True
        else:
            if nombre_alumno_binario < lista[puntoMedio].nombre:
                return busquedaBinaria(lista[:puntoMedio],nombre_alumno_binario)
            else:
                return busquedaBinaria(lista[puntoMedio+1:],nombre_alumno_binario)
#main

lista_alumnos = []
                  
print('1- Introducir los datos de los alumnos por teclado')
print('2- Dado un nombre de un alumno, buscarlo y modificar su nota, mostrando el resultado por pantalla (empleando búsqueda secuencial)')
print('3- Dado un nombre de un alumno, buscarlo y mostrar la información por pantalla empleando búsqueda binaria.')
print('4- Realizar la media de todas las notas.')
print('5- Realizar la media de las notas superiores a 5.')
print('6- Realizar la ordenación (método de selección) de los alumnos por notas en orden descendente y mostrar la nota del alumno con mejor nota. ')
print('7- Utilizando el método de inserción, realizar la ordenación de los alumnos por notas en orden ascendente y mostrar la nota del alumno que peor nota haya sacado. ')
print('0- Salir del menú.')
opcion = int(input('Introduce la opción que deseas realizar: '))

while opcion != 0:
    if opcion == 1:
        introducir_datos (lista_alumnos)                  
    elif opcion == 2:
        nombre_alumno = str(input('Nombre alumno: '))
        modificar_nota (lista_alumnos)
           
    elif opcion == 3:
        nombre_alumno_binario = str(input('Nombre alumno: '))
    elif opcion == 4:
    elif opcion == 5:
    elif opcion == 6:
    elif opcion == 7:
    opcion = int(input('\nIntroduce la opción que deseas realizar: ')) 
"""
