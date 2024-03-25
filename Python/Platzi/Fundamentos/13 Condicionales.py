if True:
    print("debería ejecutarse")

if False:
    print("nunca se ejecuta")

pet = input("¿Cual es tu mascota favorita?\n")

if pet == "perro":
    print("genial tienes buen gusto")

elif pet == "gato":
    print("espero tengas suerte")

elif pet == "pez":
    print("ere lo maximo")
else:
    print("no tienes ninguna mascota interesante")

stock = int(input("Digita el stock ->"))

if stock >= 100 and stock <= 1000:
    print("El stock es el correcto")
else:
    print("El stock es incorrecto")

