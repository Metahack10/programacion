#Proyecto: Programa que determina si un numero es par o impar
numero = int(input("Ingresa un numero: "))

if numero == 0:
    print("El numero es cero")
elif numero < 0:
    print("El numero es negativo")
elif numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")