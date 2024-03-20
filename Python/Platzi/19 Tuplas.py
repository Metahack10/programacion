numbers = (1, 2, 3, 5)
strings = ("Jorge", "Juan", "Kevin", "Jorge")
print(numbers)
print(type(numbers))
print(strings)
print(type(strings))

#Acediendo a los elementos de las tuplas
print("0 -->", numbers[0])
print("-1 -->", numbers[-1])

#Index --> Devuelve la posición del elemento indicado
print(strings.index("Kevin"))

#Count --> Devuelve la cantidad de veces que se repite el elemento indicado en la tupla
print(strings.count("Jorge"))

#List() --> Convierte la tupla en una lista
lista = list(strings)
print(lista)
print(type(lista))
lista[1] = "Pedro"
print(lista)

#Tuple() --> Convierte una lista a una tupla
tupla = tuple(lista)
print(tupla)
print(type(tupla))
