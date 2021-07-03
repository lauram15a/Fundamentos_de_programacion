#Laura Mambrilla Moreno
#Ej 1 cuaderno 5

"""
Implementa las estructuras de datos que permitan almacenar información
anónima sobre personas con objeto de hacer un estudio estadístico. Así, se
deberá almacenar el número de secuencia, sexo y edad de cada persona.
Programe además un par de funciones para (a) leer por teclado datos
relativos a una persona y (b) para mostrar dichos datos por pantalla.
"""

class Informacion:
    def __init__(self, secuencia, sexo, edad):
        self.secuencia = secuencia
        self.sexo = sexo
        self.edad = edad

def crear ():
    """
    """
    secuencia = int(input('Número de secuencia: '))
    sexo = str(input('Sexo: '))
    edad = int(input('Edad: '))
    persona = Informacion(secuencia, sexo, edad)
    return persona

def mostrar (persona):
    """
    """
    print (persona.secuencia, persona.sexo, persona.edad)


#main
persona = crear()
mostrar (persona)
