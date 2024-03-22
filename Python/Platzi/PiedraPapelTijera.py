import random

options = ("piedra", "papel", "tijera")
rondas = 1
user_win = 0
cpu_win = 0

while True:
    print("*" * 10)
    print("ROUND",rondas)
    print("*" * 10)

    print("👨  Victorias:", user_win)
    print("🖥️   Victorias:", cpu_win)

    user_option = input("🪨   piedra\n🧻  papel\n✂️   tijera\nElija una opción: ")
    user_option = user_option.lower()

    if not user_option in options:
        print("Esa opción no es valida ⚠️")
        continue

    cpu_option = random.choice(options)

    print("Opción del Usuario ->", user_option)
    print("Opción del Computador ->", cpu_option)

    if user_option == cpu_option:
        print("Empate")
    elif user_option == "piedra":
        if cpu_option == "tijera":
            print("piedra gana a tijera")
            print("el usuario ganó")
            user_win += 1
        else:
            print("papel gana a piedra")
            print("el computador ganó")
            cpu_win += 1
    elif user_option == "papel":
        if cpu_option == "piedra":
            print("papel le gana a la piedra")
            print("el usuario ganó")
            user_win += 1
        else:
            print("tijera gana al papel")
            print("el computador ganó")
            cpu_win += 1
    elif user_option == "tijera":
        if cpu_option == "papel":
            print("tijera gana a papel")
            print("el usuario ganó")
            user_win += 1
        else:
            print("piedra gana a tijera")
            print("el computador ganó")
            cpu_win += 1
    
    if cpu_win == 2:
        print("El ganador es la computadora🖥️!!!")
        break
    if user_win ==2:
        print("El ganador es el usuario 👨‍🦱!!!")
        break
    rondas += 1