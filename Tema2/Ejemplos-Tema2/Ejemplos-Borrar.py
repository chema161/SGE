##Por su índice: Mediante la sentencia del:
shopping = ['Agua' , 'Huevos' , 'Aceite' , 'Sal' , 'Limón']
del shopping[3]
print(shopping)

##Por su valor: Mediante la funcion remove():
shopping = ['Agua' , 'Huevos' , 'Aceite' , 'Sal' , 'Limón']
shopping.remove('Sal')
print(shopping)

##Por su índice (con extracción):
shopping = ['Agua' , 'Huevos' , 'Aceite' , 'Sal' , 'Limón']

product = shopping.pop() # shopping.pop(-1)
print(product)

print(shopping)

product = shopping.pop(2)
print(product)

print(shopping)

##Por su rango: Mediante troceado de listas:
shopping = ['Agua' , 'Huevos' , 'Aceite' , 'Sal' , 'Limón']
shopping[1:4] = []
print(shopping)

##Borrado completo utilizando la función clear():
shopping = ['Agua' , 'Huevos' , 'Aceite' , 'Sal' , 'Limón']
shopping.clear() # Borrado in-situ
print(shopping)

## Borrado completo 2. «Reinicializando» la lista a vacío con []:
shopping = ['Agua' , 'Huevos' , 'Aceite' , 'Sal' , 'Limón']
shopping = [] # Nueva zona de memoria
print(shopping)