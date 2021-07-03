#Crear tupla
tupla = (10, 20, 30, 40)
print(tupla)

#Crear tupla de 10 elementos con el valor 0
tupla = (0,) * 10
print(tupla)

#Acceder a un elemento
tupla = (10, 20, 30, 40)
print(tupla[2])

#Objetos inmutables
#tupla[2] = 25
    
#Concatenar tuplas
tupla = tupla + (50,)
print(tupla)

#Indice de un elemento
print(tupla.index(50))

#Agrupaciones
a = 10
b = 20
c = 30
tupla = (a,b,c)
b = 500 #No hace nada
(c,b,a) = tupla
print(a,b,c)
(a,b,c) = (c,b,a)
print(a,b,c)

#Pertenencia
print(20 in tupla)
