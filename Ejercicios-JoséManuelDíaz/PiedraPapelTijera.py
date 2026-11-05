persona1= opcion
persona2= opcion2

print('opciones')
print('1. piedra')
print('2. papel')
print('3. tijera')

opcion = int(input())

match opcion:
    case 1:
        persona1= 'piedra'
    case 2:
        persona1= 'papel'
    case 3: 
        persona1= 'tijera'

opcion2= int(input())

match opcion2:
    case 1:
        persona2= 'piedra'
    case 2:
        persona2= 'papel'
    case 3: 
        persona2= 'tijera'



    