#Laura Mambrilla Moreno
#Agenda

"""
Se pretende realizar la gestión de una agenda de reuniones, identificadas por su fecha y hora
de inicio. Cada reunión se caracteriza por tener un motivo, una lista de asistentes y una
duración. A continuación, se muestra un ejemplo de los tipos de datos necesario para
gestionar la agenda:

r1=rReunion('Planificación Programación', ['Maria', 'Juan', 'Pepe', 'Lucía'], 2)
r2=rReunion('Comisión Económica', ['Pepe', 'Lucía', 'Ana'], 1.5)
r3=rReunion('Comisión Investigación', ['Lucía', 'Miguel', 'Pablo', 'Carmen', 'Javier'], 2.5)
agenda={'31/3/2018, 10:00':r1, '1/4/2018, 9:30':r2, '1/4/2018, 15:00':r3}

Se pide:
1. Buscar la fecha y hora de la primera reunión cuyo motivo se indique.

2. Anadir un asistente a una reunión indicada por su día y hora de celebración, siempre
que no esté ya añadido.

3. Desconvocar una reunión, averiguando previamente quién participa para poder avisar.

4. Mostrar las reuniones de un día concreto.

5. Averigua la hora de finalización de la reunión más larga de un cierto día.

6. Permitir un método de introducción rápida de reuniones por el que indicando en
formato abreviado la información necesaria se guarde la reunión oportuna. Por ejemplo:

12/11/18-10:00-2-Calificación Actas-Pepe,Luis,Ana,María
crea la reunión r4, con clave '12/11/2018, 10:00'
r4=rReunion(Calificación Actas', ['Pepe', 'Luis', 'Ana', 'Maria], 2)

7. Convocar una reunión, siempre que sea posible (no hay otra ya programa a la misma
hora de inicio). Opcionalmente, compruebe si no existe solapamiento de reuniones
antes de la inserción.
"""

#Librerías
import sys


#funciones
class Reunion:
    def __init__ (self, motivo, asistentes, duracion):
        self.motivo = motivo
        self.asistentes = asistentes
        self.duracion = duracion


#1
def buscar_fecha_hora (motivo_busc, agenda):
    """
    str --> str
    OBJ: buscar fecha y hora dependiendo del motivo de la reunión
    """
    motivo_en_reunion = True
    for key,value in agenda.items(): #recorro clave y valor del dic
        if value.motivo == motivo_busc:
            motivo_en_reunion = True
            return key #no sirve for v in agenda.values() porque devolvemos keys
        else:
            motivo_en_reunion = False
    if motivo_en_reunion == False:
        mensaje = 'Motivo no encontrado.'
        return mensaje

#2
def añadir_asistente (nuevo_asistente, fecha_hora_reunion, agenda):
    """
    str, str, str, dic --> str
    OBJ: añadir asistente a una reunión si no está metido todavía
    """
    for key,value in agenda.items():
        if key == fecha_hora_reunion:
                if nuevo_asistente not in value.asistentes: 
                    value.asistentes.append(nuevo_asistente)
                return value.asistentes
                

#3
def desconvocar_reunion (motivo_desconvocar, agenda):
    """
    str --> list
    OBJ: desconvocar reunión
    """
    contador = 0
    for key,value in agenda.items():
        if value.motivo == motivo_desconvocar:
            contador += 1
            asistentes_desconvocar_reunion = value.asistentes
            desconvocar = key
            print ('\n Avisar sobre que la reunión ', motivo_desconvocar, 'se desconvoca a:')
            for i in range(len(asistentes_desconvocar_reunion)):
                print ('-',asistentes_desconvocar_reunion[i])
    if contador == 0:
        print ('\nReunión no encontrada. \n')
    else:
        del agenda[desconvocar]
        print ('\nAgenda modificada: ','\n')
    for key, value in agenda.items():
        print(key,"->",value.motivo,',', value.asistentes, ',', value.duracion)
    return agenda    

#4
def reuniones_en_un_dia (dia, agenda):
    """
    str --> str
    OBJ: mostar reuniones de un día concreto
    """
    lista_reuniones_en_dia = []
    for key,value in agenda.items():
        lista_key = key.split(',')
        dia_reuniones = lista_key[0]
        if dia_reuniones == dia:
            lista_reuniones_en_dia.append(value.motivo)
    return lista_reuniones_en_dia

#5
def duracion_mas_larga (agenda, dia_mas_larga):
    """
    str --> str
    OBJ: mostrar hora de finalización de la reunión más larga de un día
    """
    lista_duraciones = []
    lista_reuniones_en_dia = []
    for key,value in agenda.items():
        lista_key = key.split(',')
        dia_reuniones = lista_key[0]
        if dia_reuniones == dia_mas_larga:
            lista_reuniones_en_dia.append(value.motivo)
            lista_duraciones.append(value.duracion)
        else:
            lista_duraciones.append(0)
            lista_reuniones_en_dia.append('ninguna')
    #método burbuja
    for i in range (len(lista_duraciones)-1):
        for j in range(i+1,len(lista_duraciones)):
            if lista_duraciones[i] < lista_duraciones[j]:
                lista_duraciones[i],lista_duraciones[j] = lista_duraciones[j],lista_duraciones[i]
    duracion_mas_larga = lista_duraciones[0] #máxima duración
    #separo horas y minutos del 2'5
    horas_duracion = int(duracion_mas_larga)
    minutos_duracion_decimal = duracion_mas_larga - horas_duracion
    minutos_duracion = 60 * minutos_duracion_decimal
    #key, value
    contador_esta = 0
    for key,value in agenda.items():
        if value.duracion == duracion_mas_larga:
            contador_esta += 1
            lista_key = key.split(',')
            hora = lista_key[1]
            #separo horas y minutos
            horas, minutos = hora.split(':') #si pongo las variables así, horas= [0], minutos=[1]
            hora_finalizacion = int(horas) + horas_duracion
            minutos_finalizacion = int(minutos) + int(minutos_duracion)
            if minutos_finalizacion > 59:
                minutos_finalizacion -= 60
                hora_finalizacion += 1   
            #pasamos de (variable,':', variable) --> str
            hora_final=(str(hora_finalizacion),str(minutos_finalizacion))
            if minutos_finalizacion < 10:
                cadena = ":0"
            else:
                cadena = ":"
            hora_fin = cadena.join(hora_final)
            motivo = value.motivo
            duracion = value.duracion
    if contador_esta != 0:
        print('\nLa reunión sobre', motivo,', con duración de ',duracion,'h, dura hasta las ',hora_fin,'.')
    else:
        print ('\nNo hay ninguna reunión registrada en esta fecha.')
     
#6
def introduccion_rapida (formato_abreviado, agenda):
    """
    str --> dic
    OBJ: crear una reunión a partir del formato introducción rápida
    """
    fecha, hora, duracion, motivo, asistentes = formato_abreviado.split('-')
    dia, mes, anio = fecha.split('/')
    if int(anio) // 1000 < 1:
        anio = int(anio) + 2000
    sep = '/'
    fecha_cor = (dia, mes, str(anio))
    fecha_correcta = sep.join (fecha_cor)
    separador = ', '
    clave= (fecha_correcta, hora)
    tupla_clave = separador.join(clave)
    #meter asistentes en lista
    asistentes = asistentes.split(',')
    #generar r5
    r5 = Reunion(motivo, asistentes, duracion)
    agenda[tupla_clave] = r5
    return agenda

#7
def convocar_reunion_nueva (asistentes_reunion_nueva, motivo_reunion_nueva, fecha_reunion_nueva, hora_inicio_reunion_nueva, duracion_reunion_nueva, agenda):
    """
    str, str, str --> dic
    OBJ: convocar reunión nueva
    """
    fecha_hora_reunion_nueva = (fecha_reunion_nueva, hora_inicio_reunion_nueva)
    separador = ', '
    clave_reunion_nueva = separador.join(fecha_hora_reunion_nueva)
    contador = 0
    for key,value in agenda.items(): #si empieza a la misma hora en el mismo día que otra reunión
        if key == clave_reunion_nueva:
            print('\nHora ocupada. A esa hora está teniendo lugar otra reunión.')
            sys.exit(-1)
        else:
            #separo horas y mins de duración
            horas_duracion_reunion_nueva = int(duracion_reunion_nueva)
            if duracion_reunion_nueva - horas_duracion_reunion_nueva != 0:
                minutos_duracion_decimal = duracion_reunion_nueva - horas_duracion_reunion_nueva
                minutos_duracion_reunion_nueva = 60 * minutos_duracion_decimal
            #separo hora en horas y minutos de la reunion nueva
            horas_inicio_reunion_nueva, minutos_inicio_reunion_nueva = hora_inicio_reunion_nueva.split(':')
            #hora de finalizacion reunión nueva
            horas_fin_reunion_nueva =  int(horas_inicio_reunion_nueva) + horas_duracion_reunion_nueva
            if duracion_reunion_nueva - horas_duracion_reunion_nueva != 0:
                minutos_fin_reunion_nueva =  int(minutos_inicio_reunion_nueva) + minutos_duracion_reunion_nueva
            else:
                minutos_fin_reunion_nueva = minutos_inicio_reunion_nueva
            if int(minutos_fin_reunion_nueva) > 59:
                minutos_fin_reunion_nueva -= 60
                horas_fin_reunion_nueva += 1  
            #separo key en fecha y hora de las claves
            fecha, hora = key.split(',')
            #separo hora en horas y minutos de las claves
            horas, minutos = hora.split(':')
            #separo duración en horas y minutos de las claves
            duracion_valores = value.duracion
            horas_duracion = int(duracion_valores)
            if duracion_valores - horas_duracion != 0:
                minutos_duracion_decimal = duracion_valores - horas_duracion
                minutos_duracion = 60 * minutos_duracion_decimal
            else:
                minutos_duracion = 0
            if minutos_duracion > 59:
                minutos_duracion -= 60
                horas_duracion += 1 
            #hora finalizacion de las claves
            horas_fin_claves = int(horas) + horas_duracion
            minutos_fin_claves = int(minutos) + minutos_duracion
            hora_fin_claves = (str(horas_fin_claves), str(minutos_fin_claves))
            if minutos_fin_claves < 10:
                cadena = ":0"
            else:
                cadena = ":"
            hora_finalizacion_claves = cadena.join(hora_fin_claves)
            
            #comparamos
            
            if fecha == fecha_reunion_nueva:
            #hora inicio reunion nueva es igual a hora final reunion agenda
                if hora_inicio_reunion_nueva == hora_finalizacion_claves:
                    contador += 1
            #la hora de inicio de la reunion nueva se encuentra entre la hora de inicio y de fin de otra reunión
                elif int(horas) < int(horas_inicio_reunion_nueva) < horas_fin_claves:
                    print('\nHora ocupada. A esa hora está teniendo lugar otra reunión.')
                    sys.exit(-1)
                elif int(horas_inicio_reunion_nueva) == horas_fin_claves:
                    if int(minutos_inicio_reunion_nueva) < minutos_fin_claves:
                        print('Hora ocupada. A esa hora está teniendo lugar otra reunión.')
                        sys.exit(-1)
                    else:
                        contador += 1
                elif int(horas) == int(horas_inicio_reunion_nueva):
                    if int(minutos_inicio_reunion_nueva) > minutos_fin_claves:
                        print('Hora ocupada. A esa hora está teniendo lugar otra reunión.')
                        sys.exit(-1)
                    else:
                        contador += 1

            #la hora de inico reunión nueva es menor que hora inicio reunion agenda, pero termina más tarde de que empiece reunion agenda
                elif int(horas_inicio_reunion_nueva) < int(horas):
                    if int(horas_inicio_reunion_nueva) + horas_duracion_reunion_nueva > int(horas):
                        print('Hora de inicio libre pero duración muy larga: se terminaría después de que otra reunión empezase.')
                        sys.exit(-1)
                    elif int(horas_inicio_reunion_nueva) + horas_duracion_reunion_nueva == int(horas):
                        if int(minutos_inicio_reunion_nueva) > int(minutos):
                            print('Hora de inicio libre pero duración muy larga: se terminaría después de que otra reunión empezase.')
                            sys.exit(-1)
                    else:
                        contador += 1
                elif int(horas_inicio_reunion_nueva) == int(horas):
                    if int(minutos_inicio_reunion_nueva) < int(minutos):
                        if int(horas_inicio_reunion_nueva) + horas_duracion_reunion_nueva > int(horas):
                            print('Hora de inicio libre pero duración muy larga: se terminaría después de que otra reunión empezase.')
                            sys.exit(-1)
                    elif int(horas_inicio_reunion_nueva) + horas_duracion_reunion_nueva == int(horas):
                        if int(minutos_inicio_reunion_nueva) > int(minutos):
                            print('Hora de inicio libre pero duración muy larga: se terminaría después de que otra reunión empezase.')
                            sys.exit(-1)
                    else:
                        contador += 1
                        
            else:
                contador += 1

    #añadir reunión a la agenda
    if contador != 0:
        #pasamos de (variable,':', variable) --> str
        fecha_hora_inicio_reunion_nueva=(fecha_reunion_nueva, hora_inicio_reunion_nueva)
        sep = ", "
        tupla_clave = sep.join(fecha_hora_inicio_reunion_nueva)
        #generar reunión nueva
        asistentes_reunion_nueva = []
        print('\nAgenda modificada: \n')
        if duracion_reunion_nueva - int(duracion_reunion_nueva) == 0:
            duracion_reunion_nueva = int(duracion_reunion_nueva)
            r6 = Reunion(motivo_reunion_nueva, asistentes_reunion_nueva, duracion_reunion_nueva)
            agenda[tupla_clave] = r6
            for key, value in agenda.items():
                print(key,"->",value.motivo,',', value.asistentes, ',', value.duracion)
    


#MAIN

r1 = Reunion('Planificación Programación', ['María', 'Juan', 'Pepe', 'Lucía'], 3.5)

r2 = Reunion('Comisión Económica', ['Pepe', 'Lucía', 'Ana'], 1.5)

r3 = Reunion('Comisión Investigación', ['Lucía', 'Miguel', 'Pablo', 'Carmen', 'Javier'], 2.5)

r4 = Reunion('Prueba', ['Lucía', 'Miguel', 'Pablo', 'Carmen', 'Javier'], 0.5)

r7 = Reunion('Segunda Prueba', ['Lara', 'Mario', 'Dérec', 'Yara', 'Rodrigo', 'Iria'], 3)

agenda={'31/03/2018, 10:00':r1, '01/04/2018, 09:30':r2, '01/04/2018, 15:00':r3, '01/04/2018, 08:00':r4, '05/12/2018, 12:00':r7}

#menú
print('\n-------------------------------------------------')
print('                     AGENDA')
print('-------------------------------------------------')

print('\n********* MENÚ ********\n')

op1 = '      1 - Buscar la fecha y hora de la primera reunión cuyo motivo se indique.'
op2 = '     2 - Añadir un asistente a una reunión indicada por su día y hora de celebración, siempre que no esté ya añadido.'
op3 = '     3 - Desconvocar una reunión, averiguando previamente quién participa para poder avisar.'
op4 = '     4 - Mostrar las reuniones de un día concreto.'
op5 = '     5 - Hora de finalización de la reunión más larga de un cierto día.'
op6 = '     6 - Método de introducción rápida de reuniones.'
op7 = '     7 - Convocar una reunión.'
op8 = '     8 - Salir.'


print(op1,'\n', op2, '\n', op3, '\n', op4, '\n', op5, '\n', op6, '\n', op7, '\n', op8)

opcion = str(input('\n--> Opción que desea realizar: '))
print('\nHas elegido:')

while opcion != '8':

    if opcion == '1':
        print (op1)
        motivo_busc = str(input('\nMotivo: '))
        print ('La reunión ',motivo_busc,'tendrá lugar el día --> ',buscar_fecha_hora (motivo_busc, agenda))

    elif opcion == '2':
        print (op2)
        asistentes = []
        nuevo_asistente = str(input('\nNuevo asistente: '))
        fecha_hora_reunion = str(input('Fecha y hora de la reunión (dd/mm/aaaa, hh:mm): '))
        print('\nLos asistentes reunión de ', fecha_hora_reunion, ' son : ',añadir_asistente (nuevo_asistente, fecha_hora_reunion, agenda))

    elif opcion == '3':
        print (op3)
        motivo_desconvocar = str(input('\nReunión a desconvocar: '))
        desconvocar_reunion (motivo_desconvocar, agenda)

    elif opcion == '4':
        print (op4)
        dia = str(input('\nDía (dd/mm/aaaa): '))
        lista_reuniones = reuniones_en_un_dia (dia, agenda)
        print ('')
        for i in range (len(lista_reuniones)):
            print('-', lista_reuniones[i])

    elif opcion == '5':
        print (op5)
        dia_mas_larga = str(input('\nDía (dd/mm/aaaa): '))
        duracion_mas_larga (agenda, dia_mas_larga)

    elif opcion == '6':
        print (op6)
        formato_abreviado = str(input('\nFormato rápido: '))
        print('')
        agenda = introduccion_rapida (formato_abreviado, agenda)
        for key, value in agenda.items():
            print(key,"->",value.motivo,',', value.asistentes, ',', value.duracion)

    elif opcion == '7':
        print (op7)
        motivo_reunion_nueva = str(input('\nMotivo de la reunión nueva: '))
        fecha_reunion_nueva = str(input('Fecha (dd/mm/aaaa): '))
        hora_inicio_reunion_nueva = str(input('Hora de inicio (hh:mm): '))
        duracion_reunion_nueva = float(input('Duración (horas): '))
        asistentes_reunion_nueva= []
        convocar_reunion_nueva (asistentes_reunion_nueva, motivo_reunion_nueva, fecha_reunion_nueva, hora_inicio_reunion_nueva, duracion_reunion_nueva, agenda)

    else:
        print('              Opción no válida.')

    print('\n___________________________________________________________________________\n')

    print('\n-------------------------------------------------')
    print('                     AGENDA')
    print('-------------------------------------------------')

    print('\n********* MENÚ ********\n')

    print(op1,'\n', op2, '\n', op3, '\n', op4, '\n', op5, '\n', op6, '\n', op7)

    opcion = str(input('\n--> Opción que desea realizar: '))
    print('\nHas elegido:')

print('              Salir.')




























        
 
