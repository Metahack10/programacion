cadena = "Estoy aprendiendo el lenguaje de programacion de Python"
#metodo para buscar una palabra dentro de una cadena - Tomar en cuenta que las posiciones empiezan desde el 0
print(cadena.find("lenguaje"))
print(cadena.find("Estoy"))
print(cadena.find("Python"))
print(cadena[0:28].find("Python"))

#metodo para cambiar una cadena a minuscula
print(cadena.lower())

#metodo para cambiar una cadena a mayusculas
print(cadena.upper())

#metodo para cambiar a mayusculas solo la primera letra de cada palabra
print(cadena.title())

#metodo para reemplazar el contenido de una cadena
print(cadena.replace("aprendiendo", "desarrollando"))

#metodo para extraer o cortar una palabra dentro de una cadena - considerar sumarle 1 a la posicion de la ultima letra
print(cadena[6:17])
