#Los conjuntos no admiten repetidos, no tienen un orden y se pueden modificar
set_paises = {"col", "mex", "bol"}
print(set_paises)
print(type(set_paises))

set_numbers = {1,2,2,445,23}
print(set_numbers)

set_types = {1, "hola", False, 12.12}
print(set_types)

set_from_string = set("hoola")
print(set_from_string)

set_from_tuple = set(("abc", "def", "jlv", "abc"))
print(set_from_tuple)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)

# Modificando conjuntos
#Len() --> Me devuelve la cantidad de elementos que tiene el conjunto
size = len(set_paises)
print(size)

#In --> pregunta si un elemento existe dentro del conjunto y devuelve True o False
print("col" in set_paises)
print("pe" in set_paises)

#Add --> agrega un elemento al conjunto
set_paises.add("pe")
print(set_paises)
set_paises.add("pe")
print(set_paises)

#Update --> Agrega nuevos elementos al conjunto, a diferencia del Add, update permite agregar a partir de un subconjunto
set_paises.update({"ar","ecua","pe"})
print(set_paises)

#Remove --> Remueve un elemento del conjunto
set_paises.remove("col")
print(set_paises)

set_paises.remove("ar")
print(set_paises)

#Discard --> Descarta un elemento, es similar a remove solo que cuando no encuentra el elemento no genera ningun error
set_paises.discard("arg")
set_paises.discard("bol")
print(set_paises)

#Clear --> Limpia o borra todos los elementos de un conjunto
set_paises.clear()
print(set_paises)
print(len(set_paises))
