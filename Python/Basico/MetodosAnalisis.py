cadena = "Curso de Aprendizaje de Python"
print(cadena.count("de")) #Cuenta las veces que se repite una palabra

print(cadena.find("de")) #Comienza a buscar de izquierda a derecha
print(cadena.rfind("de")) #Comienza a buscar de derecha a izquierda

print(cadena.startswith("Curso")) #Devuelve True o False si la cadena comienza por la palabra indicada
print(cadena.endswith("Curso")) #Devuelva True o False si la cadena termina con la palabra indicada

numero = "abc"
print(numero.isnumeric()) #Devuelve True o False si el texto de la cadena es un numero

numero = "123455"
print(numero.isdigit()) #Devuelve True o False si el texto de la cadena esta compuesta por diigtos

numero = "12345asddddad"
print(numero.isalnum()) #Devuelve True o False si el texto de la cadena esta compuesto por numeros y letras

abecedario = "abcdefz"
print(abecedario.isalpha()) #Devuelve True o False si el texto de la cadena esta compuesto por letras