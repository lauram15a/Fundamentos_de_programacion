
#llamar al archivo
f = open('ej1.txt','r')
mensaje = f.read()
f.close()
print(mensaje)

#añadir al archivo
f = open('ej1.txt','a')
f.write('Lo hemos conseguido')
f.close()
f = open('ej1.txt','r')
mensaje = f.read()
print(mensaje)


#nos muestra lo que hay en el directorio (la carpeta donde está el archivo)
import os

print(os.listdir())

