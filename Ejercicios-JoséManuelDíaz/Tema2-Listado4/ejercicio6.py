print('Este programa lee un fichero y ofrece varias operaciones sobre su contenido.')

import random
import re

f = open('entrada.txt')

def leer_lineas():
    with f.open('r', encoding='utf-8') as archivo:
        return archivo.readlines()

def obtener_palabras(texto):
    return re.findall(r'\b\w+\b', texto.casefold())

opcion = -1

while opcion != 0:
    print('\nPulse [1] para mostrar la palabra de mayor longitud')
    print('Pulse [2] para mostrar las veces que aparece una palabra')
    print('Pulse [3] para leer una línea aleatoria del fichero')
    print('Pulse [4] para mostrar las palabras que no se repiten')
    print('Pulse [5] para añadir una línea al final del fichero')
    print('Pulse [0] para salir del programa')

    opcion = int(input('\nElija una opción: '))

    match opcion:
        case 1:
            palabras = obtener_palabras(' '.join(leer_lineas()))
            if palabras:
                mayor = max(palabras, key=len)
                print(f'La palabra de mayor longitud es: "{mayor}" ')
            else:
                print('El fichero no contiene palabras.')

        case 2:
            palabra = input('Escriba la palabra que desea buscar: ').casefold()
            veces = obtener_palabras(' '.join(leer_lineas())).count(palabra)
            print(f'La palabra aparece {veces} veces.')

        case 3:
            lineas = [linea.rstrip('\n') for linea in leer_lineas() if linea.strip()]
            if lineas:
                print(f'Línea aleatoria: {random.choice(lineas)}')
            else:
                print('El fichero no contiene líneas para mostrar.')

        case 4:
            palabras = obtener_palabras(' '.join(leer_lineas()))
            unicas = sorted({palabra for palabra in palabras if palabras.count(palabra) == 1})
            if unicas:
                print('Palabras que aparecen una sola vez:', ', '.join(unicas))
            else:
                print('No hay palabras que aparezcan una sola vez.')

        case 5:
            nueva_linea = input('Escriba el texto que desea añadir: ')
            with f.open('a', encoding='utf-8') as archivo:
                archivo.write(nueva_linea + '\n')
            print('Línea añadida correctamente.')

        case 0:
            print('Saliendo del programa...')

        case default:
            print('Opción no válida.')

print('Gracias por usar este programa')