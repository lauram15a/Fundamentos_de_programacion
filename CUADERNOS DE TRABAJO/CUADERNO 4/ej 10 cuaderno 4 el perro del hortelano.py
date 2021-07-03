#Laura Mambrilla Moreno
#Ej 10 cuaderno 4

"""
Escriba un programa que “codifique” una frase modificando todas las vocales
según el siguiente código: a por 4, e por 3, i por 1, o por 0 y u por el
símbolo #. Por ejemplo, la frase: “Un perro del hortelano”, deberá
devolverse: “#n p3rr0 d3l h0rt3l4n0”.
"""

#funciones
def cambio (frase):
    """
    cad --> cad
    """
    lista_frase = frase.split() #decomponemos la frase en palabras
    len_frase = len(lista_frase)
    for i in range (len_frase -1):
        lista_frase[i] = list(lista_frase[i])
        len_lista_en_frase = len(lista_frase[i])
        for j in range (len_lista_en_frase):
            if lista_frase[[i][j]] == 'a' or lista_frase[[i][j]] == 'A':
                lista_frase[[i][j]] = 4
            elif lista_frase[[i][j]] == 'e' or lista_frase[[i][j]] == 'E':
                lista_frase[[i][j]] = 3
            elif lista_frase[[i][j]] == 'i' or lista_frase[[i][j]]== 'I':
                lista_frase[[i][j]] = 1
            elif lista_frase[[i][j]] == 'o' or lista_frase[[i][j]] == 'O':
                lista_frase[[i][j]] = 0
            elif lista_frase[[i][j]] == 'u' or lista_frase[[i][j]] == 'U':
                lista_frase[[i][j]] = '#'
    delimitador = ''
    delimitador.join (lista_frase)
    return lista_frase
    
#main
frase = 'Un perro rarito'#str(input('Escribe un mensaje: '))
print(cambio(frase))
