#LAURA MAMBRILLA MORENO
#EJ 8 CUADERNO 3

"""
Escribe un algoritmo que tras leer tres enteros los escriba en pantalla en orden
creciente. Como siempre, valida las entradas.
"""

def validar_entero_a():
    """
    """
    try:
        a = int(input('a= '))
    except:
        print ('Número no válido')
        return False
    else:
        return a

def validar_entero_b():
    """
    """
    try:
        b = int(input('b= '))
    except:
        print ('Número no válido')
        return False
    else:
        return b

def validar_entero_c():
    """
    """
    try:
        c = int(input('c= '))
    except:
        print ('Número no válido')
        return False
    else:
        return c
        
def ordenar (a,b,c):
    """
    """
    if a>b and b>c: #a>b>c
        print (a,'>',b,'>',c)
    elif a>c and c>b: #a>c>b
        print (a,'>',c,'>',b)
    elif b>c and c>a: #b>c>a
        print (b,'>',c,'>',a)
    elif b>a and a>c: #b>a>c
        print (b,'>',a,'>',c)
    elif c>a and a>b: #c>a>b
        print (c,'>',a,'>',b)
    elif c>b and b>a: #c>b>a
        print (c,'>',b,'>',a)
        
#main
a= validar_entero_a()
b= validar_entero_b()
c= validar_entero_c()

ordenar(a,b,c)
