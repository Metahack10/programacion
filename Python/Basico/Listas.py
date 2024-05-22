Contenido = ["Curos", "Alumnos", 1025, True, 105.38, "Masculino"] #Es un vector que acepta diferentes tipos de datos, a diferencia de las tuplas que se definen con () las listas se definen por [] y se puede cambiar su contenido
print(Contenido)
Contenido[1] = "Estudiantes" #Modifica un elemento existente de la lista
print(Contenido)

print(Contenido[3])
print(Contenido[-1])
print(Contenido[0:3])
print(Contenido[:2])

Contenido.append("Python") #Agrega al final de la lista un nuevo elemento
print(Contenido)

Contenido.insert(2,"Profesor") #Inserta un nuevo elemento a la lista en la posicion indicada
print(Contenido)

Contenido.extend(["Nivel Basico", "Nivel Intermedio", "Nivel Avanzado"]) #Agrega al final de la lista una cantidad X de nuevos elementos
print(Contenido)

print(Contenido.index("Masculino")) #Busca si un elemento se encuentra en la lista, si existe devolvera la posicion y si no genera un error
#print(Contenido.index("Hacker"))

Contenido.remove("Masculino") #Elimina el elemento indicado de la lista
print(Contenido)

print(Contenido.count(1025)) #Cuenta la cantidad de veces que un elemento se repite en la lista

Contenido2 = ["Curso1", "Curso2"]
Resultado = Contenido + Contenido2 #Combina 2 listas
print(Resultado)


