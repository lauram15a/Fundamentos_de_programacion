'''
Cuaderno de trabajo 2.pdf - Ejercicio 14

Descripción: Calculadora de complejos.
'''

#Funciones
def suma(cmp1Real, cmp1Imag, cmp2Real, cmp2Imag):
    '''float,float,float,float --> float,float
       OBJ: Suma de un número complejo'''
    real = cmp1Real + cmp2Real
    imag = cmp1Imag + cmp2Imag
    return real,imag
	
def resta(cmp1Real, cmp1Imag, cmp2Real, cmp2Imag):
    '''float,float,float,float --> float,float
       OBJ: Resta de un número complejo'''
    real = cmp1Real - cmp2Real
    imag = cmp1Imag - cmp2Imag
    return real,imag
    
def producto(cmp1Real, cmp1Imag, cmp2Real, cmp2Imag):
    '''float,float,float,float --> float,float
       OBJ: Producto de un número complejo'''
    real = cmp1Real*cmp2Real - cmp1Imag*cmp2Imag
    imag = cmp1Real*cmp2Imag + cmp1Imag*cmp2Real
    return real,imag

def division(cmp1Real, cmp1Imag, cmp2Real, cmp2Imag):
    '''float,float,float,float --> float,float
       OBJ: División de un número complejo'''
    divisor = cmp2Real**2 + cmp2Imag**2
    real = (cmp1Real*cmp2Real + cmp1Imag*cmp2Imag) / divisor
    imag = (cmp1Imag*cmp2Real - cmp1Real*cmp2Imag) / divisor
    return real,imag

#Programa principal
cmp1Real = float(input("Complejo 1 (parte real): ")) 
cmp1Imag = float(input("Complejo 1 (parte imaginaria): ")) 
cmp2Real = float(input("Complejo 2 (parte real): ")) 
cmp2Imag = float(input("Complejo 2 (parte imaginaria): ")) 

resReal,resImag = suma(cmp1Real,cmp1Imag,cmp2Real,cmp2Imag)
print(f"Suma de complejos: ({resReal})+({resImag})i")
resReal,resImag = resta(cmp1Real,cmp1Imag,cmp2Real,cmp2Imag)
print(f"Resta de complejos: ({resReal})+({resImag})i")
resReal,resImag = producto(cmp1Real,cmp1Imag,cmp2Real,cmp2Imag)
print(f"Producto de complejos: ({resReal})+({resImag})i")
resReal,resImag = division(cmp1Real,cmp1Imag,cmp2Real,cmp2Imag)
print(f"División de complejos: ({resReal})+({resImag})i")
