import random
#{key:value for element in iterable}
dict = {}
for i in range(1,5):
    dict[i] = i * 2

print(dict)

dict_v2 = {i:i * 2 for i in range(1,5)}
print(dict_v2)

paises = ["col", "mex", "bol", "pe"]
poblacion = {}
for pais in paises:
    poblacion[pais] = random.randint(1,100)

print(poblacion)

poblacion_v2 = {pais:random.randint(1,100) for pais in paises}
print(poblacion_v2)

nombres = ["Nico", "Jorge", "Juan"]
edades = [12,56,98]
print(list(zip(nombres, edades)))

personas = {nombre:edad for (nombre,edad) in zip(nombres,edades)}
print(personas)

#{key:value for var in iterable if condition}
print(poblacion_v2)
poblacion_v3 = {pais:poblacion for (pais,poblacion) in poblacion_v2.items() if poblacion > 20}
print(poblacion_v3)

text = "Hola, soy Nicolas"
unique = {c:c.upper() for c in text if c in "aeiou"}
print(unique)
