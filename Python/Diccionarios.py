#Mi diccionario = {"key1":<value1>,"key2":<value2>,"keyN":<valueN>}

Persona = {"Nombre":"Jorge", "Apellido":"Lopez", "Edad":42, "Sueldo":17000}
print(Persona)
print(Persona["Sueldo"]) #Imprime directamente un elemento de la variable diccionario

Persona["Sueldo"] = 17800 # Modifica el valor de un elemento de la variable diccionario
print(Persona)

del Persona["Edad"] # Elimina un elemento de la variable diccionario especificando la clave
print(Persona)

print(Persona.get("Apellidos", "Ninguno")) # Busca y muestra el valor de la clave buscada dentro de la variable diccionario y si no existe esa clave muestra en este caso el valor Ninguno

print(Persona.keys()) # Devuelve todas las claves que tiene la variable diccionario

print(Persona.values()) # Devuelve todos los valores de las claves que tiene la variable diccionario

