#Laura Mambrilla Moreno
#Ej 3 cuaderno 5

"""
Amplíe el ejercicio anterior mostrando al final del proceso los datos
completos de la mujer y el hombre más jóvenes de todos los introducidos.
"""

class Informacion:
    def __init__(self, secuencia, sexo, edad):
        self.secuencia = secuencia
        self.sexo = sexo
        self.edad = edad

def crear ():
    """
    """    
    secuencia = int(input('\nNúmero de secuencia: '))
    sexo = str(input('Sexo: '))
    edad = int(input('Edad: '))
    persona = Informacion(secuencia, sexo, edad)
    return persona

def mostrar (persona):
    """
    """
    print (persona.secuencia, persona.sexo, persona.edad)


#main
    
edad_general = 0
num_mujeres = 0
num_hombres = 0
edad_mujeres = 0
edad_hombres = 0
num_mujeres_13_16 = 0
num_hombres_menor_20 = 0
media_edad = 0
mujer_joven = 1000000
hombre_joven = 1000000

for i in range (10):
    persona = crear()
    edad_general += persona.edad
    if persona.sexo == 'Mujer':
        num_mujeres += 1
        edad_mujeres += persona.edad
        if persona.edad >= 13 and persona.edad <= 16:
            num_mujeres_13_16 += 1
        if  persona.edad < mujer_joven:
            mujer_joven = persona.edad
            secuencia_mujer_joven = persona.secuencia
            edad_mujer_joven = persona.edad
    if persona.sexo == 'Hombre':
        num_hombres += 1
        edad_hombres += persona.edad
        if persona.edad <= 20:
            num_hombres_menor_20 += 1
        if  persona.edad < hombre_joven:
            hombre_joven = persona.edad
            secuencia_hombre_joven = persona.secuencia
            edad_hombre_joven = persona.edad
    media_edad += persona.edad/10

if num_hombres < num_mujeres:
    print ('\nLa media es de mujeres.')
if num_hombres > num_mujeres:
    print('\nLa media es de hombres.')
else:
    print('\nHay el mismo número de mujeres que de hombres.')

print ('Hay %d mujeres entre 13 y 16 años.'%num_mujeres_13_16)
print ('Hay %d hombres menores de 20 años.'%num_hombres_menor_20)
print ('La media de edad es de %d.'%media_edad)

if num_mujeres > 0:
    print ('\nDATOS MUJER MÁS JOVEN \n%d Mujer %d'%(secuencia_mujer_joven, edad_mujer_joven))
if num_hombres > 0:
    print ('','\nDATOS HOMBRE MÁS JOVEN \n%d Hombre %d'%(secuencia_hombre_joven, edad_hombre_joven))
