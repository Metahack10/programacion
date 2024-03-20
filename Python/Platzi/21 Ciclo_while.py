contador = 0

while contador < 10:
    contador += 1
    print(contador)

contador = 0

while contador < 20:
    contador += 1
    if contador == 15:
        break
    print(contador)

contador = 0

while contador < 20:
    contador += 1
    if contador < 15:
        continue
    print(contador)