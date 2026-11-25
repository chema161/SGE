from datetime import datetime

f = open('entrada.txt', 'a')
ahora = datetime.now()

f.write(ahora)
f.close()

print(f)