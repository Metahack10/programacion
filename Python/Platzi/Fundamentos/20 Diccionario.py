mi_diccionario = {}
print(type(mi_diccionario))

mi_diccionario = {
    "nombre": "Jorge",
    "apellidos": "Lopez Vicente",
    "edad": "42"
}
print(mi_diccionario)

#len() --> Devuelve la cantidad de elementos del diccionario
print(len(mi_diccionario))

#variable[] --> Se utiliza para acceder directamente al valor del elemento especificado en el diccionario
print(mi_diccionario["apellidos"])
print(mi_diccionario.get("apellidos"))
print(mi_diccionario.get("sexo")) #--> Si el elemento no existe devuelve "None" y no error a diferencia de referenciarlo con []

#In --> verifica si un elemento existe en un diccionario y devuelve True o False
print("edad" in mi_diccionario)
print("sexo" in mi_diccionario)

persona = {
    "nombre": "Jorge",
    "apellidos": "Lopez Vicente",
    "Lenguajes progracion": ["Python", "HTML"],
    "edad": 42
}
print(persona)

#Formas de actualizar los valores de los elementos de un diccionario
persona["nombre"] = "Juan Pablo"
persona["edad"] -= 20
persona["Lenguajes progracion"].append("CSS")
print(persona)

#Formas para eliminar un elemento de un diccionario
del persona["apellidos"]
persona.pop("edad")
print(persona)

#Devuelve una lista de Tuplas de keys y values de cada elementos del diccionario
print("Items")
print(persona.items())

#Devuelve una lista de todas las keys que existen en el diccionario
print("Keys")
print(persona.keys())

#Devuelve una lista de todos los valores de cada elemento del diccionario
print("Values")
print(persona.values())
