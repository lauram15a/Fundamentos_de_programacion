#Método de ordenación por inserción

def ordenacion_por_insercion (lista):
    for i in range(1,len(lista)) :
        aux=lista[i]
        j=i
        while j>0 and aux > lista[j-1]:
            lista[j]=lista[j-1]
            j-=1
        lista[j]=aux
    print (lista)

lista = [54,26,93,17,77,31,44,55,20]
ordenacion_por_insercion (lista)



  
