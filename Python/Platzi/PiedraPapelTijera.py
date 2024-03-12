user_option = input("piedra\npapel\ntijera\nElija una opción: ")
cpu_option = "papel"

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