#LAURA MAMBRILLA MORENO
#EJ 5 CUADERNO 3

"""
Programa una función “validar_real” similar a la del ejercicio anterior pero que
valide que una entrada es un número real
"""


def validar_real():
    """
    """
    n = input('Introduce un número entero: ')
    try:
       n_real = float(n)
    except ValueError:
       n_real = None
      
    if n_real == None:
       print(n, "no es un número")
    elif n_real == int(n_real):
       print(int(n_real), "es entero", )
    else:
       print(n_real, "es real",)

#main
validar_real()


