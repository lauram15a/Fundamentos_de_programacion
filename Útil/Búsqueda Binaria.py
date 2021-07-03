#Funciones
def busqueda_Binaria(lista, item):
    if len(lista) == 0:
        return False
    else:
        puntoMedio = len(lista)//2
        if lista[puntoMedio]==item:
            return True
        else:
            if item<lista[puntoMedio]:
                return busqueda_Binaria(lista[:puntoMedio],item)
            else:
                return busqueda_Binaria(lista[puntoMedio+1:],item)

#Programa principal
lista = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(busqueda_Binaria(lista, 3))
print(busqueda_Binaria(lista, 13))
