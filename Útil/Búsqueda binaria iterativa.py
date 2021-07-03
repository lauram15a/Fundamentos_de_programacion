#Búsqueda binaria

def busqueda_binaria_iterativa (v, elem ) :
    posicion = -1
    encontrado = False
    ini = 0
    fin = len (v) -1
    while (ini <= fin and not encontrado ) :
        centro = (ini + fin) //2
        if (v[ centro ] == elem ) :
            encontrado = True
            posicion = centro
        elif ( elem < v[ centro ]) :
            fin = centro -1
        else :
            ini = centro + 1
    return posicion


v = [1,2,5,6,3,4,8,3]
elem = 6
print (busqueda_binaria_iterativa (v, elem ))
