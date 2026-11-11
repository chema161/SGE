print('Saludos, este programa gestiona las notas medias de los estudiantes.')

estudiantes = {'1A': 7, '2B': 8, '3C': 6, '4D': 9, '5E': 5, '6F': 10, '7G': 4}

opcion = int(1)

while opcion != 0:

    print('\nPulse [1] para mostrar los datos')
    print('Pulse [2] para modificar la nota de un estudiante')
    print('Pulse [3] para añadir un nuevo estudiante')
    print('Pulse [4] para mostrar estudiantes por encima de una nota de corte')
    print('Pulse [0] para salir del programa')
    opcion = int(input('Seleccione una opción: '))

    match opcion:

        case 1:
            print('\nNota media')
            for dni, nota in estudiantes.items():
                print(f'{dni} - {nota}')

        case 2:
            dni = input('Introduzca el DNI del estudiante: ').upper()
            nota_actual = estudiantes.get(dni)

            match nota_actual:

                case None:
                    print('No existe ningún estudiante con ese DNI.')

                case _:
                    estudiantes[dni] = float(input('Introduzca la nueva nota: '))
                    print(f'La nueva nota media es {estudiantes[dni]:g}.')

        case 3:
            dni = input('Introduzca el DNI del nuevo estudiante: ').upper()
            nota_actual = estudiantes.get(dni)

            match nota_actual:
                case None:
                    nota = float(input('Introduzca la nota media: '))
                    estudiantes[dni] = nota
                    print(f'Estudiante añadido con nota media {nota:g}.')
                case _:
                    print('Ya existe un estudiante con ese DNI.')

        case 4:
            nota_corte = float(input('Introduzca la nota de corte: '))
            estudiantes_seleccionados = {
                dni: nota for dni, nota in estudiantes.items()
                if nota > nota_corte
            }

            print('Estudiantes con nota media superior a la nota de corte:')
            print(estudiantes_seleccionados)

        case 0:
            print('Saliendo del programa...')

        case default:
            print('Opción no válida')

print('Gracias por usar este programa.')
