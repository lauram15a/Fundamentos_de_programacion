#Laura Mambrilla Moreno
#Ejs 1, 2, 3 cuaderno 5

"""
-Los datos se deben almacenar en una lista de registros de tipo tPersona.
-Hay que hacer los tres ejercicios en el mismo fichero, con un menú que muestre
las distintas opciones (añadir persona, mostrar personas, media de edad, media por sexo, ...).
-Al terminar de ejecutar una opción se muestra otra vez el menú (habrá una opción para
salir de la aplicación). Podéis seguir el ejemplo de menu.py en  la carpeta "Práctica 5".
"""

#funciones
class Informacion:
    def __init__(self, secuencia, sexo, edad):
        self.secuencia = secuencia
        self.sexo = sexo
        self.edad = edad

def validacion_entero(entero):
    """
    float --> bool
    OBJ: Validar si el dato introducido por el usuario es un número entero
    """
    try:
        dato = int(entero)
        validacion = True
    except:
        validacion = False
    return validacion


#1
def crear ():
    """
    nada --> int, str, int
    OBJ: crear persona
    """
    #secuencia
    secuencia = input('\nNúmero de secuencia: ')
    valido_entero = validacion_entero(secuencia)
    while valido_entero == False:
        print('Num de secuencia no válido. Tiene que ser un número entero: ')
        secuencia = input('\nNúmero de secuencia: ')
        valido_entero = validacion_entero(secuencia)
    #sexo
    sexo = str(input('Sexo (Hombre/Mujer): '))
    while sexo != 'Hombre' and sexo != "Mujer":
        print('Sexo no válido. Introduzca de nuevo el sexo:')
        sexo = str(input('\nSexo (Hombre/Mujer): '))
    #edad
    edad = input('Edad: ')
    valido_entero = validacion_entero(edad)
    while valido_entero == False:
        print('Edad no válida. Tiene que ser un número entero: ')
        edad = input('\nEdad: ')
        valido_entero = validacion_entero(edad)
    #persona                
    persona = Informacion(secuencia, sexo, edad)
    return persona


#2
def secuencia_ascendente(tPersona):
    """
    int --> int
    OBJ: ordenar las personas por el número de secuencia de forma ascendente
    """
    long = len(tPersona)
    for i in range (long - 1):
        for j in range (i+1, long):
            if tPersona[i].secuencia > tPersona[j].secuencia:
                tPersona[i], tPersona[j] = tPersona[j], tPersona[i]
    return tPersona

def secuencia_descendente(tPersona):
    """
    int --> int
    OBJ: ordenar las personas por el número de secuencia de forma descendente
    """
    long = len(tPersona)
    for i in range (long - 1):
        for j in range (i+1, long):
            if tPersona[i].secuencia < tPersona[j].secuencia:
                tPersona[i], tPersona[j] = tPersona[j], tPersona[i]
    return tPersona

def mostrar_mujer(tPersona):
    """
    """
    lista_mujeres = tPersona[:]
    for i in range (len(lista_mujeres)-1, -1, -1):
        if lista_mujeres[i].sexo != 'Mujer':
            del lista_mujeres[i]
    return lista_mujeres

def mostrar_hombre(tPersona):
    """
    """
    lista_hombres = tPersona[:]
    for i in range (len(lista_hombres)-1, -1, -1):
        if lista_hombres[i].sexo != 'Hombre':
            del lista_hombres[i]
    return lista_hombres

def edad_ascendente(tPersona):
    """
    int --> int
    OBJ: ordenar las personas por edad de forma ascendente
    """
    long = len(tPersona)
    for i in range (long - 1):
        for j in range (i+1, long):
            if tPersona[i].edad > tPersona[j].edad:
                tPersona[i], tPersona[j] = tPersona[j], tPersona[i]
    return tPersona

def edad_descendente(tPersona):
    """
    int --> int
    OBJ: ordenar las personas por edad de forma descendente
    """
    long = len(tPersona)
    for i in range (long - 1):
        for j in range (i+1, long):
            if tPersona[i].edad < tPersona[j].edad:
                tPersona[i], tPersona[j] = tPersona[j], tPersona[i]
    return tPersona


#3
def mas_mujeres_hombres(tPersona):
    """
    int --> int
    OBJ: decir si hay más mujeres que hombres y viceversa
    """
    num_mujeres = 0
    num_hombres = 0
    for i in range (len(tPersona)):
        if tPersona[i].sexo == 'Mujer':
            num_mujeres += 1
        else:
            num_hombres += 1
    if num_mujeres > num_hombres:
        print ('\nHay más mujeres que hombres')
        print ('Número de mujeres --> ', num_mujeres)
        print ('Número de hombres --> ', num_hombres)
    elif num_mujeres < num_hombres:
        print ('\nHay más hombres que mujeres')
        print ('Número de hombres --> ', num_hombres)
        print ('Número de mujeres --> ', num_mujeres)
    else:
        print ('\nHay el mismo número de mujeres que de hombres --> ', num_mujeres)


#4
def media_edad_general (tPersona):
    """
    int --> float
    OBJ: calcular la edad media general
    """
    edad_general = 0
    num_personas = 0
    for i in range (len(tPersona)):
        num_personas += 1
        edad_general += tPersona[i].edad
    media_edad_general = edad_general / num_personas
    return media_edad_general
        
#5
def media_edad_mujeres(tPersona):
    """
    int --> float
    OBJ: calcular la edad media de las mujeres
    """
    edad_mujeres = 0
    num_mujeres = 0
    for i in range (len(tPersona)):
        if tPersona[i].sexo == 'Mujer':
            num_mujeres += 1
            edad_mujeres += tPersona[i].edad
    if num_mujeres != 0:
        media_mujeres = edad_mujeres / num_mujeres
        return media_mujeres
    else:
        return 0


#6
def media_edad_hombres(tPersona):
    """
    int --> float
    OBJ: calcular la edad media de los hombres
    """
    edad_hombres = 0
    num_hombres = 0
    for i in range (len(tPersona)):
        if tPersona[i].sexo == 'Hombre':
            num_hombres += 1
            edad_hombres += tPersona[i].edad
    if num_hombres != 0:
        media_hombres = edad_hombres / num_hombres
        return media_hombres
    else:
        return 0


#7
def mujeres_13_16 (tPersona):
    """
    int --> int
    OBJ: calcular cuántas mujeres tienen entre 13 y 16 años
    """
    num_mujeres_13_16 = 0
    for i in range (len(tPersona)):
        if tPersona[i].sexo == 'Mujer':
            if 13 <= tPersona[i].edad <= 16:
                num_mujeres_13_16 += 1
    return num_mujeres_13_16

#8
def hombres_menos_20 (tPersona):
    """
    int --> int
    OBJ: calcular cuántos hombres tienen menos de 20 años
    """
    num_hombres_menos_20 = 0
    for i in range (len(tPersona)):
        if tPersona[i].sexo == 'Hombre':
            if tPersona[i].edad < 20:
                num_hombres_menos_20 += 1
    return num_hombres_menos_20


#9
def mujer_mas_joven (tPersona):
    """
    int --> int, str, int
    OBJ: seleccionar a la mujer más joven
    """
    long = len(tPersona)
    lista_mujeres = []
    for i in range (long):
        if tPersona[i].sexo == 'Mujer':
            lista_mujeres.append(tPersona[i])
    for i in range(len(lista_mujeres)-1):
        for j in range(i+1,len(lista_mujeres)):
            if lista_mujeres[i].edad > lista_mujeres[j].edad:
                lista_mujeres[i],lista_mujeres[j] = lista_mujeres[j],lista_mujeres[i]
    mujer_mas_joven = lista_mujeres[0]
    return mujer_mas_joven
    

#10
def hombre_mas_joven (tPersona):
    """
    int --> int, str, int
    OBJ: seleccionar al hombre más joven
    """
    long = len(tPersona)
    lista_hombres = []
    for i in range (long):
        if tPersona[i].sexo == 'Hombre':
            lista_hombres.append(tPersona[i])
    for i in range(len(lista_hombres)-1):
        for j in range(i+1,len(lista_hombres)):
            if lista_hombres[i].edad > lista_hombres[j].edad:
                lista_hombres[i],lista_hombres[j] = lista_hombres[j],lista_hombres[i]
    hombre_mas_joven = lista_hombres[0]
    return hombre_mas_joven

#todas
def mostrar_personas(tPersona):
    """
    OBJ: mostrar personas
    """
    print('\n*PERSONAS GUARDADAS*')
    for i in range (len(tPersona)):
        print('\n--> ',i+1)
        print('Número de secuencia: ', tPersona[i].secuencia)
        print('Sexo: ', tPersona[i].sexo)
        print('Edad: ', tPersona[i].edad)
    


#main
print('\n----')
print('MENÚ')
print('----')

op1 = '\n1- Añadir persona.'
op2 = '2- Mostrar personas.'
op3 = '3- Mostrar si hay más mujeres o más hombres.'
op4 = '4- Calcular la media de edad general.'
op5 = '5- Calcular la media de edad de mujeres.'
op6 = '6- Calcular la media de edad de hombres.'
op7 = '7- Mostrar cuántas mujeres tienen entre 13 y 16 años.'
op8 = '8- Mostrar cuántos hombres tienen menos de 20 años.'
op9 = '9- Mostrar los datos completos de la mujer más joven.'
op10 = '10- Mostrar los datos completos del hombre más joven.'
op0 = '0- Salir del menú.'

print(op1)
print(op2)
print(op3)
print(op4)
print(op5)
print(op6)
print(op7)
print(op8)
print(op9)
print(op10)
print(op0)

print('\n------------------------------')
opcion = str(input('¿Qué opción desea realizar?: '))
print('------------------------------')

p5= Informacion(95, 'Hombre', 49)
p6= Informacion(357, 'Mujer', 15)
p7= Informacion(9955, 'Hombre', 19)
p8= Informacion(75, 'Mujer', 13)

tPersona = [p5, p6, p7, p8]

while opcion != '0':
    #1
    if opcion == '1':
        persona = crear()
        tPersona.append(persona)
        
    #2   
    elif opcion == '2':
        mostrar = str(input('\n¿Mostar personas por numero de secuencia, sexo, edad u orden de entrada?: '))
        #número de secuencia
        if mostrar == 'numero de secuencia':
            modo = str(input('¿ascendente o descendente?: '))
            if modo == 'ascendente':
                tPersona_modo_ascendente = secuencia_ascendente(tPersona)
                mostrar_personas(tPersona_modo_ascendente)
            elif modo == 'descendente':
                tPersona_modo_descendente = secuencia_descendente(tPersona)
                mostrar_personas(tPersona_modo_descendente)
            else:
                print('Modo no válido.')
        #sexo
        elif mostrar == 'sexo':
            sexo_mostrar = str(input('¿Mujer u Hombre?: '))
            if sexo_mostrar == 'Mujer':
                tPersona_mostrar_sexo_mujer = mostrar_mujer(tPersona)
                mostrar_personas(tPersona_mostrar_sexo_mujer)              
            elif sexo_mostrar == 'Hombre':
                tPersona_mostrar_sexo_hombre = mostrar_hombre(tPersona)
                mostrar_personas(tPersona_mostrar_sexo_hombre)
            else:
                print('Género no válido.')
        #edad
        elif mostrar == 'edad':
            modo = str(input('¿ascendente o descendente?: '))
            if modo == 'ascendente':
                tPersona_edad_ascendente = edad_ascendente(tPersona)
                mostrar_personas(tPersona_edad_ascendente)
            elif modo == 'descendente':
                tPersona_edad_descendente = edad_descendente(tPersona)
                mostrar_personas(tPersona_edad_descendente)
            else:
                print('Modo no válido.')
        #orden de entrada
        elif mostrar == 'orden de entrada':
            mostrar_personas(tPersona)
        #else   
        else:
            print('No es una opción a mostrar.')

    #3    
    elif opcion == '3':
        mas_mujeres_hombres(tPersona)

    #4    
    elif opcion == '4':
        print('\nLa media de edad general: ',media_edad_general (tPersona))

    #5    
    elif opcion == '5':
        print('\nLa media de edad de las mujeres: ',media_edad_mujeres(tPersona))

    #6   
    elif opcion == '6':
        print('\nLa media de edad de los hombres: ',media_edad_hombres(tPersona))

    #7                           
    elif opcion == '7':
        print('\nNúmero de mujeres de entre 13 y 16 años: ', mujeres_13_16 (tPersona))

    #8                         
    elif opcion == '8':
        print('\nNúmero de hombres menores de 20 años: ', hombres_menos_20 (tPersona))

    #9                         
    elif opcion == '9':
        print('\nDatos de la mujer más joven:')
        mujer_mas_joven = mujer_mas_joven (tPersona)
        print('\nNúmero de secuencia: ', mujer_mas_joven.secuencia)
        print('Sexo: ', mujer_mas_joven.sexo)
        print('Edad: ', mujer_mas_joven.edad)
        

    #10
    elif opcion == '10':
        print('\nDatos del hombre más joven:')
        hombre_mas_joven = hombre_mas_joven (tPersona)
        print('\nNúmero de secuencia: ', hombre_mas_joven.secuencia)
        print('Sexo: ', hombre_mas_joven.sexo)
        print('Edad: ', hombre_mas_joven.edad)
                               
    else:
        print('\nOpción no válida.')

    #menú
    print ('\n_______________________________________________________________________________')
    print('\n--------------------------------')
    ver_menu = str(input('¿Necesitas ver otra vez el menú? (Si / No): '))
    print('--------------------------------')

    while ver_menu != 'Si' and ver_menu != 'No':
        print('\nNo ha quedado claro si lo necesitas o no. Te lo voy a preguntar de nuevo:')
        ver_menu = str(input('¿Necesitas ver otra vez el menú? (Si / No): '))

    if ver_menu == 'Si':
        print('\n----')
        print('MENÚ')
        print('----')

        op1 = '\n1- Añadir persona.'
        op2 = '2- Mostrar personas.'
        op3 = '3- Mostrar si hay más mujeres o más hombres.'
        op4 = '4- Calcular la media de edad general.'
        op5 = '5- Calcular la media de edad de mujeres.'
        op6 = '6- Calcular la media de edad de hombres.'
        op7 = '7- Mostrar cuántas mujeres tienen entre 13 y 16 años.'
        op8 = '8- Mostrar cuántos hombres tienen menos de 20 años.'
        op9 = '9- Mostrar los datos completos de la mujer más joven.'
        op10 = '10- Mostrar los datos completos del hombre más joven.'
        op0 = '0- Salir del menú.'

        print(op1)
        print(op2)
        print(op3)
        print(op4)
        print(op5)
        print(op6)
        print(op7)
        print(op8)
        print(op9)
        print(op10)
        print(op0)
    print('\n------------------------------')
    opcion = str(input('¿Qué opción deseas realizar?: '))
    print('------------------------------')
print('\nHas salido del programa.')
