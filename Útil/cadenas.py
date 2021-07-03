#Crear cadena
cadena = "Hola Mundo"
print(cadena, "\n")

#Concatenar cadenas
cadena = "Hola"+" "+"Mundo"

#Multiplicar
print("Multiplicar")
cadena = "Hola" * 3
print(cadena, "\n")

#Longitud de una cadena
print(len(cadena), "\n")

#Acceder a un caracter
print("acceder a un caracter")
print(cadena[0], "\n")

#Buscar
print("Buscar en cadena")
cadena = "Hola Mundo"
pos = cadena.find("M")
print(pos, "\n")

#Pasar a minusculas
print("Pasar a minúsculas")
print(cadena.lower(), "\n")

#Reemplazar
print("Reemplazar")
cadena.replace("a", "aa")
print(cadena, "\n")

#Substring
print("Substring")
cadena2 = cadena[0:5]
print(cadena2, "\n")

#Dividir
print("Dividir")
cadena = "Hola Mundo"
split = cadena.split(" ")
print(split, "\n")

#Cadena a lista
print("cadena --> lista")
lista = list(cadena)
print(lista, "\n")
print("lista --> cadena")
cadena2 = "".join(lista)
print(cadena2, "\n")
