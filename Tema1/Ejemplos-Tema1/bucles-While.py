opinion = 'S'
maximoDeOpiniones = 10
numeroDeOpiniones = 0

while opinion == 'S':
    print('Que pedazo de clase')
    numeroDeOpiniones += 1
    if numeroDeOpiniones >= maximoDeOpiniones:
        print('¡Ya sabemos que te gusta esta clase leches!')
        break
    opinion = input('¿Quieres seguir opinando? (S/N): ')