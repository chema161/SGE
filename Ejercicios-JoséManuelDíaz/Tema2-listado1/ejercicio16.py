print('Saludos, este programa sirve para ayudar a analizar temperaturas registradas durante una semana')

import random

opcion = int (1)
listaTemperaturas  = [random.randint(input(print('Seleccione los dos limites')))]
media = 40

while opcion != 0:

    print('Pulse [1] para mostrar las temperaturas introducidas ')
    print('Pulse [2] calcular y mostrar la temperatura media')
    print('Pulse [3] mostrar la temperatura minima y maxima junto al dia que ocurrieron')
    print('Pulse [4] ordenar la lista de mmayor a menor temperatura')
    print('Pulse [5] mostrar cuantos dias tuvierion temperaturas por encima de la media')
    print('Pulse [6] crear una lista solo con temperaturas superior a la media')
    print('Pulse [0] para salir del programa')

    opcion = input(print('Seleccione una opcion: '))

    match opcion:

        case 1:
            print(listaTemperaturas)

        case 2:
            temperaturaMedia = sum(listaTemperaturas) / len(listaTemperaturas)
            print('La temperatura media es: ', temperaturaMedia ,' grados')

        case 3:
            print()

        case 4:
            print(sorted(listaTemperaturas))
            print()

        case 5:
            for mayorMedia in listaTemperaturas:
                print('mayorMedia')

        case 6:
            listaMedia = listaTemperaturas.copy()


        case 0:
            print('Saliendo del programa...')

        case default:
            print('Opcion no valida')

print('Gracias por usar este programa :)')