def suma_rango(inicio,fin):
    sum = 0
    for x in range(inicio,fin):
        sum +=x
    return sum

resultado = suma_rango(1,5)
print(resultado)
resultado2 = suma_rango(resultado,resultado + 10)
print(resultado2)

#Multiples retornos y Multiples argumentos

def find_volume(length=1,width=1, depth=1):
    return length * width * depth, width, "hola"

result = find_volume()
result = find_volume(width=10)
print(result)
result, width, text = find_volume(10,5,2)
print(result)
print(width)
print(text)

