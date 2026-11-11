print('Saludos, este programa analiza las ventas de 5 artículos en 4 sucursales.')

precios = []
for articulo in range(5):
    precio = float(input(f'Introduzca el precio del artículo {articulo + 1}: '))
    precios.append(precio)

cantidades = []
for articulo in range(5):
    cantidades_articulo = []
    for sucursal in range(4):
        cantidad = int(input(
            f'Cantidad vendida del artículo {articulo + 1} '
            f'en la sucursal {sucursal + 1}: '
        ))
        cantidades_articulo.append(cantidad)
    cantidades.append(cantidades_articulo)

opcion = int(1)
while opcion != 0:

    print('\nPulse [1] para ver las cantidades totales de cada artículo')
    print('Pulse [2] para ver la cantidad de artículos vendidos en la sucursal 2')
    print('Pulse [3] para ver la cantidad del artículo 3 en la sucursal 1')
    print('Pulse [4] para ver la recaudación total de cada sucursal')
    print('Pulse [5] para ver la recaudación total de la empresa')
    print('Pulse [6] para ver la sucursal de mayor recaudación')
    print('Pulse [0] para salir del programa')
    opcion = input('Elija una opción: ')

    match opcion:

        case '1':
            for articulo in range(5):
                total_articulo = sum(cantidades[articulo])
                print(f'Artículo {articulo + 1}: {total_articulo} unidades')

        case '2':
            total_sucursal = sum(cantidades[articulo][1] for articulo in range(5))
            print(f'En la sucursal 2 se vendieron {total_sucursal} artículos')

        case '3':
            print(f'Artículo 3 vendido en la sucursal 1: {cantidades[2][0]} unidades')

        case '4':
            recaudaciones = [
                sum(precios[articulo] * cantidades[articulo][sucursal]
                    for articulo in range(5))
                for sucursal in range(4)

            ]
            for sucursal, recaudacion in enumerate(recaudaciones, start=1):
                print(f'Sucursal {sucursal}: {recaudacion:.2f} €')

        case '5':
            recaudacion_total = sum(
                precios[articulo] * sum(cantidades[articulo])
                for articulo in range(5)
            )

            print(f'Recaudación total de la empresa: {recaudacion_total:.2f} €')

        case '6':
            recaudaciones = [
                sum(precios[articulo] * cantidades[articulo][sucursal]
                    for articulo in range(5))
                for sucursal in range(4)
            ]

            sucursal_maxima = recaudaciones.index(max(recaudaciones)) + 1
            print(
                f'La sucursal de mayor recaudación es la {sucursal_maxima} '
                f'({recaudaciones[sucursal_maxima - 1]:.2f} €)'
            )

        case '0':
            print('Saliendo del programa...')

        case default:
            print('Opción no válida')

print('Gracias por usar este programa.')
