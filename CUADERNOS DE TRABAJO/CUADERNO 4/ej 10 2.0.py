#Laura Mambrilla Moreno
#Ej 10 cuaderno 4

"""
Escriba un programa que “codifique” una frase modificando todas las vocales
según el siguiente código: a por 4, e por 3, i por 1, o por 0 y u por el
símbolo #. Por ejemplo, la frase: “Un perro del hortelano”, deberá
devolverse: “#n p3rr0 d3l h0rt3l4n0”.
"""

def cambiar_vocales (frase):
    """
    str --> str
    OBJ: cambia las vocales por : a-4 e-3 i-1 o-0 u-#
    """
    dic = {'a':'4','A':'4', 'e':'3','E':'3', 'i':'1','I':'1', 'o':'0','O':'0', 'u':'#','U':'#'}
    aux = ""
    for letra in frase: #recorre la frase sin necesidad de crear lista
        if letra in dic.keys(): #las vocales las cambia en correspondencia con dic
            aux = aux + dic[letra]
        else:
            aux = aux + letra #añade la siguiente letra sin modificar nada
    return aux

#main
frase= 'Un perro rarito'
print (cambiar_vocales (frase))
