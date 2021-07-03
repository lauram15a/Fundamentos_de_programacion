#LAURA MAMBRILLA MORENO
#EJ 4 CUADERNO 3

"""
Como habrás observado, muy a menudo necesitamos validar la información
introducida por el usuario. Programa una función “validar_entero” que se asegure
de que una entrada del usuario es un entero. Ten en cuenta que dicha entrada
puede ser cualquier cosa, por ejemplo un valor real, un booleano o incluso una
cadena como “Hola”. Nuestra función recibirá un texto y retornará verdadero si es
un entero (dando por válida la entrada) o falso (rechazando la entrada).
"""

def validar_entero():
    """
    """
    try:
        x = int(input('Escribe algo: '))
        
    except:
        print ('¿Es un entero lo que has escrito?')
        return False
    else:
        print ('¿Es un entero lo que has escrito?')
        return True

#main
print(validar_entero())
