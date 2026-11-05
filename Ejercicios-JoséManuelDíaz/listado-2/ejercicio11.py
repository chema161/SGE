print('Saludos, este programa sirve para enseñar diferentes formas de mostrar listas')

def leer_lista(nombre):
    texto = input(f"Introduce las palabras de la {nombre} lista: ")
    return texto.split()

lista1 = leer_lista("primera")
lista2 = leer_lista("segunda")

conjunto1 = set(lista1)
conjunto2 = set(lista2)

todas = []
for p1, p2 in zip(lista1, lista2):
    for palabra in (p1, p2):
        if palabra not in todas:
            todas.append(palabra)

n = min(len(lista1), len(lista2))
for palabra in lista1[n:] + lista2[n:]:
    if palabra not in todas:
        todas.append(palabra)

print("\nPalabras en las dos listas: ", sorted(conjunto1 & conjunto2))
print("Palabras solo en la primera: ", sorted(conjunto1 - conjunto2))
print("Palabras solo en la segunda:  ", sorted(conjunto2 - conjunto1))
print("Todas las palabras de ambas listas: ", todas)

print('\nGracias por usar este programa')