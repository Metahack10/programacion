numbers = [1, 2, 3, 4, 5]
print(numbers[2])
numbers[-1] = 10
print(numbers)

#Append --> agrega un elemento al final de la lista
numbers.append(700)
print(numbers)

#Insert --> Agrega un elemento a la lista en la posicion indicada
numbers.insert(0, "hola")
print(numbers)
numbers.insert(3, "change")
print(numbers)

# + --> el operador mas sirve para fusionar las listas
tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks
print(new_list)

#Index --> devuelve la posicion del elemento buscado
index = new_list.index("todo 2")
new_list[index] = "todo change"
print(new_list)

#Remove --> Elimina de la lista el elemento indicado
new_list.remove("todo 1")
print(new_list)

#POP --> Elimina el ultimo elemento de una lista, si es que no se especifica ninguna posicion
new_list.pop()
print(new_list)
new_list.pop(3)
print(new_list)

#Reverse --> Cambia o invierte el orden de los elementos de la lista
new_list.reverse()
print(new_list)

#Sort --> Ordena el orden de los elementos de la lista
numbers_a = [1,4,6,3]
numbers_a.sort()
print(numbers_a)

strings = ["re", "ab", "ed"]
strings.sort()
print(strings)

