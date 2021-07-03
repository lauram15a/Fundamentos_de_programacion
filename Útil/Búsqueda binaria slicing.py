
#Búsqueda binaria con Slicing

def busqueda_binaria_rec (v, elem ):
    """ lista , obj -> int
    OBJ : Busca un elemento en un vector y retorna su posicion , -1 si no se encuentra
    PRE : El vector debe estar ordenado """
    centro = len (v) // 2
    if (v[ centro ] == elem ):
        pos = centro
    else :
        if ( len (v) == 1) :
            pos = -1
        elif ( elem < v[ centro ]) :
            pos = busqueda_binaria_rec (v [0: centro ], elem )
        else :
            pos = busqueda_binaria_rec (v[ centro +1: len (v)] , elem )
    # la posicion en el subvector + centro + 1 sera la posicion en el vector original ...
            pos += centro + 1
    return pos
