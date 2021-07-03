
#funciones
def serie (n):
    """
    int --> float
    OBJ: calcular serie
    """
    numerador = 0
    elem = 1
    for i in range (n):
        #numerador
        if i == 0:
            numerador = 1
            denominador = 1
            elem = 1
        else:
            if numerador // ((-1)*numerador) == 1: #numerador negativo
                numerador = numerador * (-1)
            numerador = numerador + 1
            if numerador % 2 == 0: #numerador par
                numerador = numerador * (-1)
            #denominador
            denominador = numerador - 1
            factorial = 1
            if denominador == 0:
                elem = 1
            else:
                for j in range (1, denominador + 1):
                    factorial = factorial * j
            #elem
            elem = numerador / factorial
    #s
    if elem // ((-1)*elem) == 1: #elem negativo
        elem = elem +((numerador-1)/(factorial/(n)))
        print (elem)
    else: #elem positivo
        elem = elem -((numerador-1)/(factorial/(n)))
        print (elem)
            
    


#main
n = int(input('Num elementos serie= '))
serie (n)
