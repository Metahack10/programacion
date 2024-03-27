import random

def choose_options():
    options = ("piedra", "papel", "tijera")

    user_option = input("🪨   piedra\n🧻  papel\n✂️   tijera\nElija una opción: ")
    user_option = user_option.lower()

    if not user_option in options:
        print("Esa opción no es valida ⚠️")
        return None, None

    cpu_option = random.choice(options)
    print("Opción del Usuario ->", user_option)
    print("Opción del Computador ->", cpu_option)

    return user_option, cpu_option

def check_rules(user_option, cpu_option, user_win,cpu_win):
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
    return user_win, cpu_win

def check_winner(user_win,cpu_win):
    bandera = False
    if cpu_win == 2:
       print("El ganador es la computadora🖥️!!!")
       bandera = True
    if user_win ==2:
        print("El ganador es el usuario 👨‍🦱!!!")
        bandera = True
    return bandera

def run_game():
    user_win = 0
    cpu_win = 0
    rondas = 1

    while True:
        print("*" * 10)
        print("ROUND",rondas)
        print("*" * 10)

        print("👨  Victorias:", user_win)
        print("🖥️   Victorias:", cpu_win)
        user_option, cpu_option = choose_options()
        if (user_option and cpu_option) == None:
            continue
        user_win, cpu_win = check_rules(user_option,cpu_option,user_win,cpu_win)
        gameover = check_winner(user_win,cpu_win)
        if gameover:
            break
        rondas += 1

run_game()