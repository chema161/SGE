
print ('Saludos, este programa genera un numero aleatorio entre 0 a 10 y el usuario debe tratar de adivinarlo en 3 intentos')

import random

numero = random.randint(0, 10)
intentos_maximos = 3
intentos = 0
acertado = False

print("Elige un número entre 0 y 10. Tienes 3 intentos para adivinarlo")

while intentos < intentos_maximos and not acertado:
    intento = int(input("Introduce tu número: "))
    intentos += 1

    if intento == numero:
        acertado = True
        print(f"Has acertado")

    if not acertado and intentos < intentos_maximos:
        print(f"Te quedan {intentos_maximos - intentos} intento(s).")

if not acertado:
    print(f"Has perdido. El número era {numero}.")

print('Gracias por usar este programa :)')