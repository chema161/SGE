print('Saludos, esta aplicación funciona como una calculadora en la que puedes realizar operaciones')

boton = int(1)
while boton != 0 :
    
    print('[1] para sumar ') 
    print('[2] para restar ') 
    print('[3] para multiplicar ') 
    print('[4] para dividir ') 
    print('[0] para salir del programa ')
    boton = int(input('Elija una opcion ')) 

    if boton == 1:
        suma1 = float(input('eliga el primer numero '))
        suma2 = float(input('eliga el segundo numero '))
        totalSuma = suma1 + suma2
        print(totalSuma)

    if boton == 2:
        resta1 = float(input('eliga el primer numero '))
        resta2 = float(input('eliga el segundo numero '))
        totalResta = resta1 - resta2
        print(totalResta)

    if boton == 3:
        mult1 = float(input('eliga el primer numero '))
        mult2 = float(input('eliga el segundo numero '))
        totalMult = mult1 * mult2
        print(totalMult)

    if boton == 4:
        div1 = float(input('eliga el dividendo '))
        div2 = float(input('eliga el divisor '))
        totalDiv = div1 / div2
        print(totalDiv)

    if boton == 0:
        print('Saliendo del programa...')