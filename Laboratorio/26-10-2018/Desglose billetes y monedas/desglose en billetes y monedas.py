#DESGLOSE BILLETES Y MONEDAS


#funciones
def desglose (cantidad):
    """
    int --> int
    OBJ: Desglose en billetes y monedas
    """
    #500
    num_500 = cantidad // 500
    resto_500 = cantidad % 500
    if num_500 > 0:
        print('Billetes de 500 € : ', num_500)
    #200
    num_200 = resto_500 // 200
    resto_200 = resto_500 % 200
    if num_200 > 0:
        print('Billetes de 200 € : ', num_200)
    #100
    num_100 = resto_200 // 100
    resto_100 = resto_200 % 100
    if num_100 > 0:
        print('Billetes de 100 € : ', num_100)
    #50
    num_50 = resto_100 // 50
    resto_50 = resto_100 % 50
    if num_50 > 0:
        print('Billetes de 50 € : ', num_50)
    #20
    num_20 = resto_50 // 20
    resto_20 = resto_50 % 20
    if num_20 > 0:
        print('Billetes de 20 € : ', num_20)
    #10
    num_10 = resto_20 // 10
    resto_10 = resto_20 % 10
    if num_10 > 0:
        print('Billetes de 10 € : ', num_10)
    #5
    num_5 = resto_10 // 5
    resto_5 = resto_10 % 5
    if num_5 > 0:
        print('Billetes de 5 € : ', num_5)
    #2
    num_2 = resto_5 // 2
    resto_2 = resto_5 % 2
    if num_2 > 0:
        print('Monedas de 2 € : ', num_2)
    #1
    num_1 = resto_2 // 1
    resto_1 = resto_2 % 1
    if num_1 > 0:
        print('Monedas de 1 € : ', num_1)

#main
cantidad= int(input('\nIntroduzca la cantidad de dinero: '))
print('')
desglose (cantidad)
