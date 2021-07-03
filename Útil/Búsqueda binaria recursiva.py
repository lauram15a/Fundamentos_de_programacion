#Búsqueda binaria recursiva

def busqueda_binaria_rec (v, elem , ini , fin ):
    centro = (ini+ fin) // 2
    if (v[ centro ] == elem ):
        pos = centro
    else :
        if ( ini >fin) :
            pos = -1
        elif ( elem < v[ centro ]) :
            pos = busqueda_binaria_rec (v, elem , ini , centro -1 )
        else :
            pos = busqueda_binaria_rec (v, elem , centro +1 , fin )
    return pos
