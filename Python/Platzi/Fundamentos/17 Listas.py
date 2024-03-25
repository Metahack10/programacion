numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ["lavar los platos", "jugar videojuegos"]
print(tasks)

types = [1, True, "hola"]
print(types)

print(numbers[0]) #Se obtiene el primer elemento de la lista
print(tasks[0])
tasks[0] = "Ver los cursos de platzi"
print(tasks)

print(numbers[:3]) #Imprime los 3 primeros elementos de la lista del 0 al 2 
print(True in types) #Devuelve True si existe el elemento indicado en la lista
print("hola" in types)
