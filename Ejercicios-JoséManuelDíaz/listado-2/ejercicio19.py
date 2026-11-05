print('Saludos, este programa es un menu que ayuda a leer precios y cantidades vendidas de productos en 4 sucursales de una empresa')

opc = int(1)
while opc != 0:
    print('pulse [1] para ver las cantidades totales de cada articulo')
    print('pulse [2] para ver la cantidad de articulos en la sucursal 2')
    print('pulse [3] para ver la cantidad del articulo 3 en la sucursal 1')
    print('pulse [4] para ver la recaudación total de cada sucursal')
    print('pulse [5] para ver la recaudacion total de la empresa')
    print('pulse [6] para ver la sucursal de mayor recaudación')
    print('pulse [0] para salir del programa')
    opcion = input(f'\nElija una opción: ')

    match opc:
        case 1:
            print('')

        case default :
            print('Opcion no valida')

print('Gracias por usar este programa')