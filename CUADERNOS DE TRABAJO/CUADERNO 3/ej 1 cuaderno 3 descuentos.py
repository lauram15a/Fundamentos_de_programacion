
#LAURA MAMBRILLA MORENO
#EJ 1 - CUADERNO 3

"""
Escribe un código que implemente el siguiente comportamiento: “Si la compra es
superior a 100EUR se aplica un descuento del 5% si se paga al contado, pero si el
pago es con tarjeta sólo se aplica el 2%”. Asegúrate de que el importe de la
compra es un número válido antes de proceder a los cálculos (pista: usa try para
comprobar que es posible convertir la entrada a un float).
"""

# IMPORTE --> float
def comprobar_float():
    """
    float --> bool
    OBJ: comprobar que el importe es un float
    """
    try:
        importe = float(input ('Introduce el importe: '))
    except:
        print ('El importe introducido no es válido')
        return 0
    else:
        return importe
 
# MODO DE PAGO --> str
def validar_modo_pago ():
    """
    #str --> bool
    #OBJ: modo_pago== 'Efectivo' or modo_pago== 'Tarjeta'
    """
    try:
        modo_pago = str(input('Introduce el modo de pago (Efectivo/Tarjeta): '))
    except :
        print ('El modo de pago introducido no es válido')
        return 0
    else:
        return modo_pago

#main
importe= comprobar_float()
modo_pago= validar_modo_pago()

if importe >= 0:
    if importe > 100:
        if modo_pago == 'Efectivo':
            pago = importe - importe*5/100
            print ('Debe pagar %.2f €' %pago)
        elif modo_pago == 'Tarjeta':
            pago = importe - importe*2/100
            print ('Debe pagar %.2f €' %pago)
        else:
            print ('Ese modo de pago no es una opción')
    else:
        if modo_pago == 'Tarjeta' :
            print ('Debe pagar %.2f €' %importe)
        elif modo_pago == 'Efectivo':
            print ('Debe pagar %.2f €' %importe)
        else:
            print ('Ese modo de pago no es una opción')
else:
    print ('El importe no puede ser negativo')

