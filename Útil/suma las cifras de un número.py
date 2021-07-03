#Código que suma las cifras de un número

def suma_cifras (n):
    """
    float --> int
    """
    i = 0
    while n != 0:
        i = i + n % 10
        n = n // 10
    return i

#main
n = int (input('Introduzca un número: '))
print(suma_cifras (n))
