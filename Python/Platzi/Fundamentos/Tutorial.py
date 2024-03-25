#Tutorial para el uso del bucle for aplicado a las matematicas

Numero = int(input("Escoge el numero de la tabla de multiplicar que quieres generar: "))
for x in range(1,11):
    print(Numero, "×", x, " = ", Numero * x)