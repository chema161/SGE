##Creación de tuplas
tupla_vacia = ()

tenerife_geoloc = (28.46824, -16.25462)
three_wise_men = ( 'Melchor' , 'Gaspar' , 'Baltasar' )

##Tuplas de un elemento
one_item_tuple = ( 'Papá Noel' )
print(one_item_tuple)

print(type(one_item_tuple))

one_item_tuple = ( 'Papá Noel', )
print(one_item_tuple)

print(type(one_item_tuple))

##Tuplas sin paréntesis
one_item_tuple = 'Papá Noel',

three_wise_men = 'Melchor', 'Gaspar', 'Baltasar'

tenerife_geoloc = 28.46824, -16.25462

##Modificar una tupla
##three_wise_man = 'Melchor', 'Gaspar', 'Baltasar'

##three_wise_man[0] = 'Tom Hanks'

##Conversión
shopping = ['Agua', 'Aceite', 'Arroz']

print(tuple(shopping))

##print(tuple(5))

##Operaciones con tuplas 
## reverse()
## append()
## extend()
## remove()
## clear()
## sort()

##Desempaquetado de tuplas
three_wise_men = ( 'Melchor' , 'Gaspar' , 'Baltasar' )
king1, king2, king3 = three_wise_men

print(king1)
print(king2)
print(king3)

quoting, remainder = divmod(7, 3)

print(quoting)
print(remainder)

##intercambio de valores
value1 = 40
value2 = 20

value1, value2 = value2, value1

print(value1)
print(value2)

##Desempaquetado extendido
ranking = ('G', 'A', 'R', 'Y', 'W')
head, *body, tail = ranking

print(head)
print(body)
print(tail)

##Desempaquetado generico
##sobre cadenas de textos
oxygen = 'O2'
first, last = oxygen

print(first, last)

text = 'Hello, World!'
head, *body, tail = text

print(head, body, tail)

##sobre listas
writer1, writer2, writer3 = [ 'Virginia Woolf', 'Jane Austen', 'Mary Shelley' ]
print(writer1, writer2, writer3)

text = 'Hello, World!'
word1, word2 = text.split()
print(word1, word2)

##Tuplas por compresion
myrange = (number for number in range(1, 6))

print(myrange)