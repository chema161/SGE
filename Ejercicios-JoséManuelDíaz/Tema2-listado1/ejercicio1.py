print('Saludos, este programa muestra una lista de numeros y reemplaza los negativos con 0')
numeros = [5, -3, 8, -1, 0, 12, -7, 4, -9, 6]

print("Lista original:", numeros)

for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = 0

print("Lista modificada:", numeros)

print('Gracias por usar este programa')