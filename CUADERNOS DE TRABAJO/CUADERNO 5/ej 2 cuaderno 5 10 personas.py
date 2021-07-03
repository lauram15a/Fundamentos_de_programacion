#Laura Mambrilla Moreno
#Ej 2 cuaderno 5

"""
Sin utilizar listas, programa un software que utilice lo programado en el
ejercicio 1 para leer la edad de 10 personas y calcular la media de edad
general, la media por sexo, la cantidad de mujeres que tienen entre 13 y 16
años y el número de hombres menores de 20 años.

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

for i in range (4):
    persona = crear()
    edad_general += persona.edad
    if persona.sexo == 'Mujer':
        num_mujeres += 1
        edad_mujeres += persona.edad
        if persona.edad >= 13 and persona.edad <= 16:
            num_mujeres_13_16 += 1
    if persona.sexo == 'Hombre':
        num_hombres += 1
        edad_hombres += persona.edad
        if persona.edad <= 20:
            num_hombres_menor_20 += 1
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





















            
        
