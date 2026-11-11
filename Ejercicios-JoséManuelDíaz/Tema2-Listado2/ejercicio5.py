print('Saludos, este programa permite realizar operaciones con un conjunto de números enteros.')

numeros = set()
cantidad = int(input('¿Cuántos números desea introducir?: '))

for posicion in range(cantidad):
    numero = int(input(f'Introduzca el número {posicion + 1}: '))
    numeros.add(numero)

opcion = int (1)
while opcion != 0:

    print('\nConjunto actual:', numeros)
    print('Pulse [1] para añadir el número 15')
    print('Pulse [2] para eliminar el número 9')
    print('Pulse [3] para calcular la cantidad de elementos')
    print('Pulse [4] para comprobar si el 6 está en el conjunto')
    print('Pulse [0] para salir del programa')
    opcion = input('Seleccione una opción: ')

    match opcion:

        case '1':
            numeros.add(15)
            print('Se ha añadido el número 15.')

        case '2':
            match 9 in numeros:

                case True:
                    numeros.remove(9)
                    print('Se ha eliminado el número 9.')

                case False:
                    print('El número 9 no se encuentra en el conjunto.')

        case '3':
            print(f'El conjunto tiene {len(numeros)} elementos.')

        case '4':
            match 6 in numeros:

                case True:
                    print('El número 6 está en el conjunto.')

                case False:
                    print('El número 6 no está en el conjunto.')

        case '0':
            print('Saliendo del programa...')

        case default:
            print('Opción no válida.')

print('Gracias por usar este programa.')