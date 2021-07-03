def aumenta(a):
    print('Dentro:', id(a))
    a[0] += 1
    print('Dentro:', id(a))
    print('Dentro:', a)
    return a

#Programa principal
a = [3]
print('Fuera:', id(a))
print('Fuera:', a)
aumenta(a)
print('Fuera:', id(a))
print('Fuera:', a)
a = aumenta(a)
print('Fuera:', id(a))
print('Fuera:', a)
