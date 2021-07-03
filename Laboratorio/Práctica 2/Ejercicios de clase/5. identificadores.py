def aumenta(a):
    print('Dentro: %d' %id(a))
    a += 1
    print('Dentro: %d' %id(a))
    print('Dentro: %d' %a)
    return a

#Programa principal
a = 3
print('Fuera: %d'%id(a))
print('Fuera: %d'%a)
aumenta(a)
print('Fuera: %d'%id(a))
print('Fuera: %d'%a)
a = aumenta(a)
print('Fuera: %d'%id(a))
print('Fuera: %d'%a)
