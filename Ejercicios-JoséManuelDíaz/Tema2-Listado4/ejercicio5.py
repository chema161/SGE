from pathlib import Path


carpeta = Path(__file__).parent
fichero_origen = carpeta / 'datos.txt'
fichero_destino = carpeta / 'invertido.txt'

with fichero_origen.open('r', encoding='utf-8') as archivo:
	contenido = archivo.read()

lineas = contenido.splitlines()
contenido_invertido = '\n'.join(reversed(lineas))
if lineas and contenido.endswith(('\n', '\r')):
	contenido_invertido += '\n'

with fichero_destino.open('w', encoding='utf-8') as archivo:
	archivo.write(contenido_invertido)

print(f'Se han escrito las líneas en orden inverso en {fichero_destino.name}.')

