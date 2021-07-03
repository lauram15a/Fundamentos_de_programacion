#ej 1


#librerías
import random

#estructura

class Personaje:
    def __init__ (self, nombre, vida):
        self.nombre = nombre
        self.vida = vida


class Arma:
    def __init__ (self, nombre_arma, danio):
        self.nombre_arma = nombre_arma
        self.danio = danio

#funciones

#3
def ataque (lista_personajes, diccionario, personajes_vivos2):
    """
    list, dic --> str
    OBJ: ataques entre jugadores
    """
    n=0
    m=1
    j1 = lista_personajes[n]
    j2 = lista_personajes[m]
    vueltas = 1
    while j1.vida >= 0 or j2.vida >= 0:
        if vueltas == 1:
            jugadora = j1
            jugadorb = j2
            print(j1.nombre,' ataca a ',j2.nombre,end=' ')
        else:
            jugadora = j2
            jugadorb = j1
            print(j2.nombre,' ataca a ',j1.nombre,end=' ')

        for key, value in diccionario.items():
            if key == jugadora.nombre:
                armaa = value
                danio = armaa.danio
                vida_jb = jugadorb.vida - danio
                jugadorb.vida = vida_jb
        print('con el arma ',armaa.nombre_arma,'. Le hace ',danio,'daños y le deja con ',jugadorb.vida,' vida.')
        vueltas *= -1

    if vueltas == -1:
        print(j1.nombre,' ha matado a ',j2.nombre)
        del personajes_vivos2[n]
    else:
        print(j2.nombre,' ha matado a ',j1.nombre)
        del personajes_vivos2[m]


#4

def posiciones_aleatorias (personajes_vivos):
    """
    liat --> tpl
    OBJ: seleccionar dos jugadores aleatoriamente
    """
    posicion1 = random.randrange(0,len(personajes_vivos))
    posicion2 = random.randrange(0,len(personajes_vivos))
    while posicion2 == posicion1:
        posicion2 = random.randrange(0,len(personajes_vivos))

    j1 = personajes_vivos[posicion1]
    j2 = personajes_vivos[posicion2]

    tupla = (j1, j2)
    return tupla

#5
def simulacion_batalla (lista_personajes, personajes_vivos):
    """
    """
    while len(personajes_vivos) >= 2:
        tupla = posiciones_aleatorias (personajes_vivos)
        nombre_j1 = tupla[0].nombre
        nombre_j2 = tupla[1].nombre
        for i in range (len(personajes_vivos)):
            if nombre_j1 == personajes_vivos[i].nombre:
                n= i
            if nombre_j2 == personajes_vivos[i].nombre:
                m= i
        j1 = personajes_vivos[n]
        j2 = personajes_vivos[m]
        vueltas = 1
        while j1.vida >= 0 or j2.vida >= 0:
            if vueltas == 1:
                jugadora = j1
                jugadorb = j2
                print(j1.nombre,' ataca a ',j2.nombre,end=' ')
            else:
                jugadora = j2
                jugadorb = j1
                print(j2.nombre,' ataca a ',j1.nombre,end=' ')
    
            for key, value in diccionario.items():
                if key == jugadora.nombre:
                    armaa = value
                    danio = armaa.danio
                    vida_jb = jugadorb.vida - danio
                    jugadorb.vida = vida_jb
            print('con el arma ',armaa.nombre_arma,'. Le hace ',danio,'daños y le deja con ',jugadorb.vida,' vida.')
            vueltas *= -1

        if vueltas == -1:
            print(j1.nombre,' ha matado a ',j2.nombre)
            for i in range (len(personajes_vivos)):
                if j2.nombre == personajes_vivos[i].nombre:
                    muerte = i
            del personajes_vivos[muerte]
                
        else:
            print(j2.nombre,' ha matado a ',j1.nombre)
            for i in range (len(personajes_vivos)):
                if j1.nombre == personajes_vivos[i].nombre:
                    muerte = i
            del personajes_vivos[muerte]
    print ('Partida terminada')

        
    

#main


lista_personajes = []

personajes_vivos2 = []

personaje1 = Personaje('Paco',32)
personaje2 = Personaje('Manolo',45)
personaje3 = Personaje('Ana',54)
personaje4 = Personaje('Juan',60)
personaje5 = Personaje('Sandra',80)

lista_personajes.append(personaje1)
lista_personajes.append(personaje2)
lista_personajes.append(personaje3)
lista_personajes.append(personaje4)
lista_personajes.append(personaje5)

personajes_vivos2.append(personaje1)
personajes_vivos2.append(personaje2)
personajes_vivos2.append(personaje3)
personajes_vivos2.append(personaje4)
personajes_vivos2.append(personaje5)

personajes_vivos = personajes_vivos2[:]

arma1 = Arma('Primera',20)
arma2 = Arma('Segunda',10)
arma3 = Arma('Tercera',30)
arma4 = Arma('Cuarta',40)
arma5 = Arma('Quinta',50)

diccionario = {'Paco':arma1, 'Manolo':arma2, 'Ana':arma3, 'Juan':arma4, 'Sandra':arma5}

#3
#ataque (lista_personajes, diccionario, personajes_vivos)

#4
#print('')
#for i in range (len(posiciones_aleatorias (lista_personajes))):
    #print(posiciones_aleatorias (lista_personajes)[i].nombre,'-->',posiciones_aleatorias (lista_personajes)[i].vida)

#5
print('')
simulacion_batalla (lista_personajes, personajes_vivos)
