#LAURA MAMBRILLA MORENO
#EJ 6 CUADERNO 3

"""
Escribe una función que a partir de un número real y de un número entero calcule
el valor del primero elevado al segundo sin usar el operador potencia **, ni la
función pow(). Reutiliza las funciones de los apartados 5 y 6.
"""

def validar_real():
    """
    """
    try:
        n = float(input('Base= ')) #si es un float también funciona el programa
    except:
        print ('Número no válido')
        return False
    else:
        return n

def validar_entero():
    """
    """
    try:
        m = int(input('Exponente= '))
    except:
        print ('Número no válido')
        return False
    else:
        return m
    

def potencia_por_multiplicacion(n,m):
    """
    int, int --> int
    OBJ: crear una lista con m elementos (0,m-1), rellenar los elementos con n y sumar los elementos
    """
    if n==0:
        return 0
    elif m==0:
        return 1
    elif n==1:
        return n
    elif n>0 and m>0: #base y exponente positivos
        lista=[] #creo lista
        mult_componentes_lista = 1
        for i in range (0,m): #la longitud de la lista es m
            lista.append(n) #relleno la lista, siendo n todos los elementos
            mult_componentes_lista = mult_componentes_lista * lista[i]  #suma de todos los elementos de la lista
        return mult_componentes_lista
    elif n<0 and m<0:  #base y exponente negativos
        m=abs(m)
        lista=[]
        mult_componentes_lista = 1
        for i in range (0,m):
            lista.append(n)
            mult_componentes_lista = mult_componentes_lista * lista[i]
        if m%2==0:
            return 1/mult_componentes_lista
        else:
            return 1/mult_componentes_lista
    else:
        if n<0: #base negativa, exponente positivo
            lista=[]
            mult_componentes_lista = 1
            for i in range (0,m):
                lista.append(n)
                mult_componentes_lista = mult_componentes_lista * lista[i]
            return mult_componentes_lista
        else: #base positiva, exponente negativo
            m=abs(m)
            lista=[]
            mult_componentes_lista = 1
            for i in range (0,m):
                lista.append(n)
                mult_componentes_lista = mult_componentes_lista * lista[i]
            return 1/mult_componentes_lista
                
            


#main
print ('n^m')
n= validar_real()
m= validar_entero()
print (n,'^',m,'=',potencia_por_multiplicacion(n,m))
