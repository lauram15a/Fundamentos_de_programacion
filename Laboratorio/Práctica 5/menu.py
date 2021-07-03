'''
Implementación de un menú en python mediante un diccionario de funciones
'''

#Funciones
def tema_1():
    print('Hola, soy el tema 1\n')
def tema_2():
    print('Hola, soy el tema 2\n')
def tema_3():
    print('Hola, soy el tema 3\n')
def tema_4():
    print('Hola, soy el tema 4\n')
    
# Programa principal
temas = {
    1: tema_1,
    2: tema_2,
    3: tema_3,
    4: tema_4
}
tema = 1;
while (tema>0):
    print('-----------------------------------------------')
    print('Laboratorio de Fundamentos de la Programacion')
    print('-----------------------------------------------')
    print('1.- Tema 1: Primeros programas.')
    print('2.- Tema 2: Sentencias condicionales.')
    print('3.- Tema 3: Bucles.')
    print('4.- Tema 4: Funciones y Procedimientos.')
    print('')
    print('0.- Salir')
    print('-----------------------------------------------')
    tema = int(input('Selecciona un tema: '))
    print('')
    if (tema>0):
        if tema in temas:
            func = temas.get(tema)
            func()
        else:
            print('ERROR: El tema seleccionado no existe!')
print('Adiós.')
