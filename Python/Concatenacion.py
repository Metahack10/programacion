Nombre = "Jorge"
Apellido = "Lopez"
Especialidad = "Hacker"
#1ra forma concatenacion
print(Nombre + Apellido) 

#2da forma concatenacion
print("Mi nombre es: %s " %Nombre)
print("Mi nombre es: %s y Mi Apellido es: %s " %(Nombre,Apellido))

#3ra forma concatenacion
print("Mi nombre es: {0}".format(Nombre))
print("Mi nombre es: {0} y mi especialidad es: {1}".format(Nombre,Especialidad))

#4ta forma de concatenacion
print("Mi nombre es: {a} y mi Apellido es: {b}".format(a=Nombre, b=Apellido))
