#Funciones
def busquedaBinaria(lista, item):
    if len(lista) == 0:
        return False
    else:
        puntoMedio = len(lista)//2
        if lista[puntoMedio]==item:
            return True
        else:
            if item<lista[puntoMedio]:
                return busquedaBinaria(lista[:puntoMedio],item)
            else:
                return busquedaBinaria(lista[puntoMedio+1:],item)

#Programa principal
listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(busquedaBinaria(listaPrueba, 3))
print(busquedaBinaria(listaPrueba, 13))
