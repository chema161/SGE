print('Saludos, este programa es un menu con diccionarios usando claves de dni')

opc = int(1)
dni = {1:6, 2:5, 3:9, 4:1, 5:6, 6:7, 7:2}

print('Pulse [1] para mostrar los datos')
print('Pulse [2] para modificar la nota')
print('Pulse [3] para añadir un nuevo estudiante')
print('Pulse [4] para crear un diccionario solo con la nota media mayor a una dada por el usuario')
print('Pulse [0] para salir del programa')

opc = int(input('Selecciona una opción: '))

while opc != 0:

    match opc:

        case 1:
            print(dni)

        case 0:
            print('Saliendo del programa...')
            
        case default:
            print('Opcion no valida')

print('Gracias por usar este programa')