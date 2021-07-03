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
    print (duracion_mas_larga)
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
