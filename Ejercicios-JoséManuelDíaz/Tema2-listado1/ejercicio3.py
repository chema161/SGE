print('Saludos, este programa muestra notas a modo boletin y más cosas como la nota media')

cantidadNotas = int(input('¿Cuántas notas va a introducir? '))

while cantidadNotas <= 0:
	cantidadNotas = int(input('Debe introducir al menos una nota. ¿Cuántas notas va a introducir? '))

notas = []

for i in range(cantidadNotas):
	nota = float(input('Introduzca una nota entre 0 y 10: '))

	while nota < 0 or nota > 10:
		nota = float(input('La nota debe estar entre 0 y 10. Introdúzcala de nuevo: '))

	notas.append(nota)

print('\nBoletín de calificaciones')
for i, nota in enumerate(notas, start=1):
	print('Nota', i, ':', nota)

print('Nota media:', sum(notas) / len(notas))
print('Nota más alta:', max(notas))
print('Nota más baja:', min(notas))
print('Número de suspensos:', sum(1 for nota in notas if nota < 5))

print('Gracias por usar este programa')