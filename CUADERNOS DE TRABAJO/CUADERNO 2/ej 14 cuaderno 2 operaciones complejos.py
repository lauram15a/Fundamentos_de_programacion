
#Ejercicio 14 - Cuaderno 2

"""
Un número complejo es un número de la forma a+bi, donde a y b son números reales y el valor de i es √−1 . Las cuatro operaciones aritméticas básicas sobre números complejos se definen como:
 Suma: (a+bi)+(c+di)=(a+c)+(b+d)i
 Resta: (a+bi)-(c+di)=(a-c)+(b-d)i
 Producto: (a+bi)*(c+di)=(ac-bd)+(ad+bc)i
 División: (a+bi)/(c+di) = ((ac+bd)/(c2+d2)) + ((bc-ad)/(c2+d2))i, suponiendo c2+d2<>0
Programa funciones, para cada una de las operaciones descritas, y posteriormente, realiza un programa probador que lea dos números complejos y muestre por pantalla el resultado de las operaciones reseñadas.
"""

print('Nº complejo 1 --> a,b*i ; Nº complejo 2 --> c,d*i')

a = int (input( 'a= '))
b = int (input( 'b= '))
c = int (input( 'c= '))
d = int (input( 'd= '))

i = (-1)**(1/2)


def suma_complejos (a,b,c,d):
    """
    int,int,int,int --> bool
    OBJ: suma de 2 complejos
    """
    return a+c, b+d


def resta_complejos (a,b,c,d):
    """
    int,int,int,int --> bool
    OBJ: resta de 2 complejos
    """
    return a-c, b-d


def producto_complejos (a,b,c,d):
    """
    int,int,int,int --> bool
    OBJ: producto de 2 complejos
    """
    return a*c-b*d , a*d+b*c


def division_complejos (a,b,c,d):
    """
    int,int,int,int --> bool
    OBJ: comprobar si se cumple la propiedad de la división de complejos
    PRE: c**2 + d**2 <> 0
    """
    return (a*c+b*d)/(c**2+d**2) , (b*c-a*d)/(c**2+d**2)


suma_parte_real, suma_parte_compleja = suma_complejos(a,b,c,d)
resta_parte_real, resta_parte_compleja = resta_complejos(a,b,c,d)
producto_parte_real, producto_parte_compleja = producto_complejos(a,b,c,d)
division_parte_real, division_parte_compleja = division_complejos(a,b,c,d)

def negativos ():
    """float, float --> float
    OBJ: si la parte compleja es negativa, que salga restando en vez de sumando
    """
    if b+d<0: #1 #suma negativa
        print ("La suma (%.3f+%.3fi)+(%.3f+%.3fi) es (%.3f%.3fi)"%(a,b,c,d,suma_parte_real, suma_parte_compleja))               #+ #1-2i
        if b-d<0: #1.1 #resta negativa
            print ('La resta (%.3f+%.3fi)-(%.3f+%.3fi) es (%.3f%.3fi)'%(a,b,c,d,resta_parte_real, resta_parte_compleja))            #- #1-2i
            if a*d+b*c<0: #1.1.1 #producto negativo
                print ('El producto (%.3f+%.3fi)*(%.3f+%.3fi) es (%.3f%.3fi)'%(a,b,c,d,producto_parte_real, producto_parte_compleja))   #* #1-2i
                if (b*c-a*d)/(c**2+d**2)<0: #1.1.1.1 #división negativa
                    print ('La division (%.3f+%.3fi)/(%.3f+%.3fi) es (%.3f%.3fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))   #/ #1-2i
                else: #1.1.1.2 #división positiva
                    print ('La division (%.3f+%.3fi)/(%.3f+%.3fi) es (%.3f+%.3fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))  #/ #1+2i
            else: #1.1.2 #producto positivo
                print ('El producto (%.3f+%.3fi)*(%.3f+%.3fi) es (%.3f+%.3fi)'%(a,b,c,d,producto_parte_real, producto_parte_compleja))  #* #1+2i
                if (b*c-a*d)/(c**2+d**2)<0: #1.1.2.1 #división negativa
                    print ('La division (%.3f+%.3fi)/(%.3f+%.3fi) es (%.3f%.3fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))   #/ #1-2i
                else: #1.1.2.2 #división positiva
                    print ('La division (%.3f+%.3fi)/(%.3f+%.3fi) es (%.3f+%.3fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))  #/ #1+2i
        else: #1.2 #resta positiva
            print ('La resta (%.3f+%.3fi)-(%.3f+%.3fi) es (%.3f+%.3fi)'%(a,b,c,d,resta_parte_real, resta_parte_compleja))           #- #1+2i
            if a*d+b*c<0: #1.2.1 #producto negativo
                print ('El producto (%.3f+%.3fi)*(%.3f+%.3fi) es (%.3f%.3fi)'%(a,b,c,d,producto_parte_real, producto_parte_compleja))   #* #1-2i
                if (b*c-a*d)/(c**2+d**2)<0: #1.2.1.1 #división negativa
                    print ('La division (%.3f+%.3fi)/(%.3f+%.3fi) es (%.3f%.3fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))   #1-2i
                else: #1.2.1.2 #división positiva
                    print ('La división (%.3f+%.3fi)/(%.3f+%.3fi) es (%.3f+%.3fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))  #1+2i
            else: #1.2.2 #producto positivo
                print ('El producto (%.3f+%.3fi)*(%.3f+%.3fi) es (%.3f+%.3fi)'%(a,b,c,d,producto_parte_real, producto_parte_compleja))  #1+2i
                if (b*c-a*d)/(c**2+d**2)<0: #1.2.2.1 #división negativa
                    print ('La division (%.3f+%.3fi)/(%.3f+%.3fi) es (%.3f%.3fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))   #1-2i
                else: #1.2.2.2 #división positiva
                    print ('La division (%.3f+%.3fi)/(%.3f+%.3fi) es (%.3f+%.3fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))  #1+2i

    else: #2 #suma positiva
        print ('La suma (%.3f+%fi)+(%f+%fi) es (%f+%fi)'%(a,b,c,d,suma_parte_real, suma_parte_compleja))               #+ #1-2i
        if b-d<0: #2.1 #resta negativa
            print ('La resta (%f+%fi)-(%f+%fi) es (%f%fi)'%(a,b,c,d,resta_parte_real, resta_parte_compleja))            #- #1-2i
            if a*d+b*c<0: #2.1.1 #producto negativo
                print ('El producto (%f+%fi)*(%f+%fi) es (%f%fi)'%(a,b,c,d,producto_parte_real, producto_parte_compleja))   #* #1-2i
                if (b*c-a*d)/(c**2+d**2)<0: #2.1.1.1 #división negativa
                    print ('La division (%f+%fi)/(%f+%fi) es (%f%fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))   #/ #1-2i
                else: #2.1.1.2 #división positiva
                    print ('La division (%f+%fi)/(%f+%fi) es (%f+%fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))  #/ #1+2i
            else: #2.1.2 #producto positivo
                print ('El producto (%f+%fi)*(%f+%fi) es (%f+%fi)'%(a,b,c,d,producto_parte_real, producto_parte_compleja))  #* #1+2i
                if (b*c-a*d)/(c**2+d**2)<0: #2.1.2.1 #división negativa
                    print ('La division (%f+%fi)/(%f+%fi) es (%f%fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))   #/ #1-2i
                else: #2.1.2.2 #división positiva
                    print ('La division (%f+%fi)/(%f+%fi) es (%f+%fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))  #/ #1+2i
        else: #2.2 #resta positiva
            print ('La resta (%f+%fi)-(%f+%fi) es (%f+%fi)'%(a,b,c,d,resta_parte_real, resta_parte_compleja))           #- #1+2i
            if a*d+b*c<0: #2.2.1 #producto negativo
                print ('El producto (%f+%fi)*(%f+%fi) es (%f%fi)'%(a,b,c,d,producto_parte_real, producto_parte_compleja))   #* #1-2i
                if (b*c-a*d)/(c**2+d**2)<0: #2.2.1.1 #división negativa
                    print ('La division (%f+%fi)/(%f+%fi) es (%f%fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))   #1-2i
                else: #2.2.1.2 #división positiva
                    print ('La división (%f+%fi)/(%f+%fi) es (%f+%fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))  #1+2i
            else: #2.2.2 #producto positivo
                print ('El producto (%f+%fi)*(%f+%fi) es (%f+%fi)'%(a,b,c,d,producto_parte_real, producto_parte_compleja))  #1+2i
                if (b*c-a*d)/(c**2+d**2)<0: #2.2.2.1 #división negativa
                    print ('La division (%f+%fi)/(%f+%fi) es (%f%fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))   #1-2i
                else: #2.2.2.2 #división positiva
                    print ('La division (%f+%fi)/(%f+%fi) es (%f+%fi)'%(a,b,c,d,division_parte_real, division_parte_compleja))  #1+2i


negativos()

















