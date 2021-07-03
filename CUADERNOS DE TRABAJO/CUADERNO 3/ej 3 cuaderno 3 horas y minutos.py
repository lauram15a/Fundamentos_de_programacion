#LAURA MAMBRILLA MORENO
#EJ 3 CUADERNO 3

"""
Escribe un programa que lea la hora en notación de 24 horas y la devuelva en
notación de 12 horas (ejemplo: las 18:30 serán las 6:30 PM). Valida las entradas
para asegurarte de que se trata de valores en el rango correcto.

"""

def validar_entrada_hora ():
    """
    OBJ: validar entrada y marcar rango para el formato hora
    """
    hora=-1 #para que la hora entre en el bucle
    while hora<0:
        try:
            hora= int(input('Hora: '))
        except ValueError:
            print ('Dato incompatible. Introduzca otra hora: ')
    if hora>0 or hora<23:
        return hora
    return 'Fuera del rango del formato "horas"'

def validar_entrada_minutos ():
    """
    OBJ: validar entrada y marcar rango para el formato hora
    """
    minutos=-1
    while minutos<0:
        try:
            minutos= int(input('Minutos: '))
        except ValueError:
            print ('Dato incompatible. Introduzca otros minutos: ')
    if minutos>0 or minutos<23:
        return minutos
    return 'Fuera del rango del formato "horas"'

def cambio_hora(hora):
    """
    int, int --> int
    OBJ: pasar de formato AM  a PM
    """
    if hora>12:
        hora_pm = hora - 12
        if minutos<10:
            print (hora_pm,': 0',minutos,' PM')
        else:
            print (hora_pm,':',minutos,' PM')
    else:
        if minutos<10:
            print (hora,': 0',minutos,' AM')
        else:
            print (hora,':',minutos,' AM')
       

#MAIN

print ('Introduzca una hora')
hora= validar_entrada_hora()
minutos= validar_entrada_minutos()

cambio_hora(hora)
        
