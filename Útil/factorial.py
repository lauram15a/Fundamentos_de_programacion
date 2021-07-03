#Funciones
def factorial(n):
   if (n < 1):   #Caso Base
       print("Caso Base, n=1")
       return 1
   else:         #Caso Recursivo
       print(f"Caso recursivo, n={n}") 
       resultado = n * factorial(n-1)
       print(f"{n}! = {resultado}")
       return resultado

#Programa principal
print(f"El factorial de 6 es: {factorial(6)}")
