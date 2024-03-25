text = "Ella sabe programar en python"
print("JavaScript" in text) # Busca una cadena dentro de la variable text
print("python" in text)

if "python" in text:
    print("Elegiste bien!!!")
else:
    print("Tambien elegiste bien")

size = len(text) #Devuelve el valor del tamaño de la cadena
print(size)

print(text)
print(text.upper()) #Upper --> pone todo el texto a mayuscula
print(text.lower()) #Lower --> pone todo el texto a minuscula
print(text.count("a")) #Count --> cuenta cuantas veces se repite una palabra
print(text.swapcase()) #Swapcase --> convierte las mayusculas a minusculas y las minusculas a mayusculas
print(text.startswith("Ella")) #Startwith --> devuelve True si es que la cadena empieza con la palabra indicada
print(text.endswith("Rust")) #Endwith --> devuelve True si es que la cadena termina con la palabra indicada
print(text.replace("python","Go")) #Replace --> busca y reemplaza la palabra indicada por la palabra establecida.

text2 = "este es un titulo"
print(text2)
print(text2.capitalize()) #Capitalize --> convierte la primera letra del inicio de la cadena en mayuscula
print(text2.title()) #Tittle --> Convierte la primera letra de inicio de una palabra en mayuscula
print(text2.isdigit()) #Isdigit --> Me devuelve True si el texto de la cadena es un digito
print("398".isdigit())
