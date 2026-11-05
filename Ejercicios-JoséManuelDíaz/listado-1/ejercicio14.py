
print('Buenas, este programa genera un triangulo de asteriscos con la cantiad de filas que diga el usuario')

num = int(input('Diga la cantidad de filas: '))

for i in range(1, num + 1):
    print('*' * i)
    
for i in range(num - 1, 0, -1):
    print('*' * i)

print('Gracias por usar el programa')
    