import random

user_option = input("piedra\npapel\ntijera\nElija una opción: ")
user_option = user_option.lower()
options = ("piedra", "papel", "tijera")
cpu_option = random.choice(options)

print("Opción del Usuario ->", user_option)
print("Opción del Computador ->", cpu_option)

if user_option == cpu_option:
    print("Empate")
elif user_option == "piedra":
    if cpu_option == "tijera":
        print("piedra gana a tijera")
        print("el usuario ganó")
    else:
        print("papel gana a piedra")
        print("el computador ganó")
elif user_option == "papel":
    if cpu_option == "piedra":
        print("papel le gana a la piedra")
        print("el usuario ganó")
    else:
        print("tijera gana al papel")
        print("el computador ganó")
elif user_option == "tijera":
    if cpu_option == "papel":
        print("tijera gana a papel")
        print("el usuario ganó")
    else:
        print("piedra gana a tijera")
        print("el computador ganó")
else:
    print("opción no determinada")