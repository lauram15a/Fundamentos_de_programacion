#LAURA MAMBRILLA MORENO
#Ej 1 Cuaderno 7

"""
Implemente un programa, que dado un número finito de fechas, nos permita
buscar una fecha por año, mes o día, así como la ordenación de las mismas
por año. Nota: emplee el método de búsqueda binaria.
"""

class Fecha:
    def __init__(self, anio, mes, dia):
        self.dia = dia
        self.mes = mes
        self.anio = anio
                

def pedir_fecha ():
    """
    """
    dia = int(input('\nDía (dd): '))
    mes = int(input('Mes (mm): '))
    anio = int(input('Año (aaaa): '))   
    fecha = Fecha(anio, mes, dia)
    return fecha

def fecha_mayor(fecha1, fecha2):
    """
    """
    #años iguales
    if fecha1.anio == fecha2.anio:
        #meses iguales
        if fecha1.mes == fecha2.mes:
            #dias iguales
            if fecha1.dia == fecha2.mes:
                return False
            #dia1 > dia2
            elif fecha1.dia > fecha2.dia:
                return False
            #dia1 < dia2
            else:
                return False   
        #mes1 > mes2
        elif fecha1.mes > fecha2.mes:
            return True
        #mes1 < mes2
        else:
            return False
            
    #año1 > año2
    elif fecha1.anio > fecha2.anio:
        return True
    #año1 < año2
    else:
        return False
        

def ordenar_lista(lista_fecha):
    """
    """
    n = len(lista_fecha)
    for i in range(n-1):
        for j in range(i+1,n):
            if fecha_mayor(lista_fecha[i], lista_fecha[j]):
                lista_fecha[i],lista_fecha[j] = lista_fecha[j],lista_fecha[i]

def imprimir_lista (lista_fecha):
    """
    """
    for i in lista_fecha:
        print ('\n%d/%d/%d'%(i.dia, i.mes, i.anio))
    
def buscar_dia(lista_fecha, dia_buscar):
    """
    """
    lista_fecha = ordenar_lista_dia()
    posicion = -1
    encontrado = False
    inicio = 0
    fin = len (lista_fecha) - 1
    while inicio <= fin and encontrado == True :
        centro = (inicio + fin) // 2
        if lista_fecha[centro].dia == dia_buscar:
            encontrado = True
            posicion = centro
        elif dia_buscar < lista_fecha[centro].dia:
            fin = centro - 1
        else:
            ini = centro + 1
    return lista_fecha[posicion]

def buscar_mes(lista_fecha, mes_buscar):
    """
    """
    posicion = -1
    encontrado = False
    inicio = 0
    fin = len (lista_fecha) - 1
    while inicio <= fin and encontrado == True :
        centro = (inicio + fin) // 2
        if lista_fecha[centro].mes == mes_buscar:
            encontrado = True
            posicion = centro
        elif mes_buscar < lista_fecha[centro].mes:
            fin = centro - 1
        else:
            ini = centro + 1
    return lista_fecha[posicion]

def buscar_annio(lista_fecha, anio_buscar):
    """
    """
    posicion = -1
    encontrado = False
    inicio = 0
    fin = len (lista_fecha) - 1
    while inicio <= fin and encontrado == True :
        centro = (inicio + fin) // 2
        if lista_fecha[centro].anio == anio_buscar:
            encontrado = True
            posicion = centro
        elif anio_buscar < lista_fecha[centro].anio:
            fin = centro - 1
        else:
            ini = centro + 1
    return lista_fecha[posicion]

def imprimir_fecha(busqueda):
    if busqueda == 'dia':
        fecha = buscar_dia(lista_fecha, dia_buscar)
    elif busqueda == 'mes':
        fecha = buscar_mes(lista_fecha, mes_buscar)
    elif busqueda == 'anio':
        fecha = buscar_annio(lista_fecha, anio_buscar)
    print ('\nLa fecha buscada es : %d/%d/%d'%(fecha.dia, fecha.mes, fecha.anio))

#main
n = int(input('\nNúmero de las fechas que vas a introducir: '))

lista_fecha = []

for i in range (n):
    fecha = pedir_fecha()
    lista_fecha.append(fecha)

ordenar_lista(lista_fecha)

imprimir_lista(lista_fecha)

busqueda = str(input('\nBuscar por (dia, mes o anio): '))
if busqueda == 'dia':
    dia_buscar = int(input('Día que buscar: '))
    buscar_dia(lista_fecha, dia_buscar)
elif busqueda == 'mes':
    mes_buscar = int(input('Mes que buscar: '))
    buscar_mes(lista_fecha, mes_buscar)
elif busqueda == 'anio':
    anio_buscar = int(input('Anio que buscar: '))
    buscar_anio(lista_fecha, anio_buscar)
else:
    print('Opción no válida.')

imprimir_fecha(busqueda)


