#ej 2

#estructuras
class Arma :
    def __init__(self, nombre, categoria, rareza):
        self.nombre = nombre
        self.categoria = categoria
        self.rareza = rareza

#funciones

def ordenar (mochila, diccionario):
    """
    list --> list
    OBJ: Ordenar las armas de más raras a menos raras
    """
    mochila2 = mochila[:]
    for key, value in diccionario.items():
        for i in range (len(mochila2)):
            if mochila2[i].rareza == key:
                mochila[value-1] = mochila2[i]
    for i in range (len(mochila)):
        print(mochila[i].nombre,'-->',mochila[i].categoria,'-->',mochila[i].rareza)
                    


#main
mochila = []

arma1 = Arma('Primera','fusil','comun')
arma2 = Arma('Segunda', 'subfusil', 'poco comun')
arma3 = Arma('Tercera', 'ametralladora', 'epica')
arma4 = Arma('Cuarta', 'lanzador', 'legendaria')
arma5 = Arma('Quinta', 'rifle', 'rara')

mochila.append(arma1)
mochila.append(arma2)
mochila.append(arma3)
mochila.append(arma4)
mochila.append(arma5)

diccionario = {'comun':5, 'poco comun':4, 'rara':3, 'epica':2, 'legendaria':1}

ordenar (mochila, diccionario)
