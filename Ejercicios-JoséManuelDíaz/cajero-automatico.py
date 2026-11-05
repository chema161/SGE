print('Saludos, este programa esta basado en un cajero automatico con siferentes opciones para realizar')

opc = int(1)
entradas = 150.25
saldo = 1000

print('Pulse [1] para ver saldo ')
print('Pulse [2] para retirar saldo ')
print('Pulse [3] para comprar entradas ')
print('Pulse [4] para ingresar dinero ')
print('Pulse [0] para salir del programa')
opc = int(input('Elija una opción '))

while opc != 0:
    match opc :

        case 1:
            print('Su saldo actual es: ', saldo)

        case 2:
            retirar = float(input('Cuanto quiere retirar? '))
            saldo - retirar

        case 3:
            entradasCompradas = int(input('¿Cuantas entradas quiere comprar? '))
            entradasCompradas * entradas 
            saldo - entradas

        case 4:
            ingresado = float(input('Cuanto quiere ingresar '))
            ingresado + saldo

        case 0:
            print('Saliendo del programa...')
