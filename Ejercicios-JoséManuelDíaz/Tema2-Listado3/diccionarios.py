print('Saludos, este programa muestra un diccionario de palabras y expresiones con significados especiales en inglés.')

diccionario = {
    'chapuza': 'Botched job; shoddy work.',
    'flipar': 'To be amazed; to freak out (informal).',
    'morro': 'Cheek; nerve (to have the gall to do something).',
    'currar': 'To work (informal).',
    'mola': 'It is cool; it is great (informal).',
}

opcion = int(1)
while opcion != 0:

    print('\nPulse [1] para agregar una palabra')
    print('Pulse [2] para imprimir el diccionario completo')
    print('Pulse [3] para buscar una palabra')
    print('Pulse [4] para modificar el significado de una palabra')
    print('Pulse [5] para agregar sus dos palabras favoritas')
    print('Pulse [6] para borrar una palabra')
    print('Pulse [7] para ordenar el diccionario alfabéticamente')
    print('Pulse [0] para salir')
    opcion = input('Seleccione una opción: ')

    match opcion:

        case '1':
            palabra = input('Introduzca la palabra: ').strip().casefold()
            match palabra in diccionario:
                case True:
                    print('Esa palabra ya está en el diccionario.')

                case False:
                    significado = input('Introduzca su significado: ').strip()
                    diccionario[palabra] = significado
                    print('Palabra agregada.')

        case '2':
            print('\nDICCIONARIO')
            for palabra, significado in diccionario.items():
                print(f'{palabra.capitalize()}: {significado}')

        case '3':
            palabra = input('Introduzca la palabra que desea buscar: ').strip().casefold()
            significado = diccionario.get(palabra)
            match significado:
                case None:
                    print('La palabra no se encuentra en el diccionario.')
                case _:
                    print(f'{palabra.capitalize()}: {significado}')

        case '4':
            palabra = input('Introduzca la palabra que desea modificar: ').strip().casefold()
            significado = diccionario.get(palabra)
            match significado:

                case None:
                    print('La palabra no se encuentra en el diccionario.')

                case _:
                    nuevo_significado = input('Introduzca el nuevo significado: ').strip()
                    diccionario[palabra] = nuevo_significado
                    print('Significado modificado.')

        case '5':
            palabras_favoritas = {}
            for numero in range(1, 3):
                palabra = input(f'Introduzca su palabra favorita {numero}: ').strip().casefold()
                significado = input(f'Introduzca su significado de: ').strip()
                palabras_favoritas[palabra] = significado

            diccionario.update(palabras_favoritas)
            print('Las palabras favoritas se han combinado con el diccionario.')

        case '6':
            palabra = input('Introduzca la palabra que desea borrar: ').strip().casefold()
            significado = diccionario.pop(palabra, None)
            match significado:

                case None:
                    print('La palabra no se encuentra en el diccionario.')

                case _:
                    print(f'Se ha borrado "{palabra}".')

        case '7':
            diccionario = dict(sorted(diccionario.items()))
            print('Diccionario ordenado alfabéticamente.')

        case '0':
            print('Saliendo del programa...')

        case default:
            print('Opción no válida.')

print('Gracias por usar este programa.')