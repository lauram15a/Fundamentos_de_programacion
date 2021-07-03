#LAURA MAMBRILLA MORENO
#Ej 2 Cuaderno 3

"""
Escribe un subprograma que calcule el producto de dos números enteros leídos
desde el teclado sin utilizar el operador de multiplicación *. Ej: si recibe 2 y 3
devuelve 6; si recibe 2 y 0 devuelve 0; si recibe -3 y 2 dará -6. El programa no
asumirá que los números son mayores que cero, debiendo validar las entradas.
"""

def validar_entero_n():
    """
    """
    try:
        n = int(input('n= ')) #si es un float también funciona el programa
    except:
        print ('Número no válido')
        return False
    else:
        return n

def validar_entero_m():
    """
    """
    try:
        m = int(input('m= '))
    except:
        print ('Número no válido')
        return False
    else:
        return m
    

def multiplicacion_por_suma(n,m):
    """
    int, int --> int
    OBJ: crear una lista con m elementos (0,m-1), rellenar los elementos con n y sumar los elementos
    """
    if m==0 or n==0:
        return 0
    elif m==1:
        return n
    elif n==1:
        return m
    elif n>0 and m>0: #n y m positivos
        lista=[] #creo lista
        suma_componentes_lista = 0
        for i in range (0,m): #la longitud de la lista es m
            lista.append(n) #relleno la lista, siendo n todos los elementos
            suma_componentes_lista = suma_componentes_lista + lista[i]  #suma de todos los elementos de la lista
        return suma_componentes_lista
    elif n<0 and m<0:
        n=abs(n)
        m=abs(m)
        lista=[]
        suma_componentes_lista = 0
        for i in range (0,m):
            lista.append(n)
            suma_componentes_lista = suma_componentes_lista + lista[i]
        return suma_componentes_lista
    else:
        if n<0: #n negativo, m positivo
            n=abs(n)
            lista=[]
            suma_componentes_lista = 0
            for i in range (0,m):
                lista.append(n)
                suma_componentes_lista = suma_componentes_lista + lista[i]
            return -1 * suma_componentes_lista
        else: #n positivo, m negativo
            m=abs(m)
            lista=[]
            suma_componentes_lista = 0
            for i in range (0,m):
                lista.append(n)
                suma_componentes_lista = suma_componentes_lista + lista[i]
            return -1 * suma_componentes_lista
            


#main
print ('n*m')
n= validar_entero_n()
m= validar_entero_m()
print (n,'*',m,'=',multiplicacion_por_suma(n,m))



                

