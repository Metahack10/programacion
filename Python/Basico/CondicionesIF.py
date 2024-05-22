nEdad = int(input("Ingrese su edad: "))
# Ejemplo de estructura del If - Else
if nEdad >= 18: 
    print("Tu eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejemplo de estructura del If - Elif - Else
if nEdad < 18:
    print("Eres menor de edad")
elif nEdad == 18:
    print("Tu edad es 18 años")
else:
    print("Eres mayor de edad por encima de los 18 años")

# Operadores Logicos: and, or y not
# Ejemplo con AND
if nEdad >=1 and nEdad <= 10:
    print("Es un niño")
elif nEdad > 10 and nEdad < 18:
    print("Es un adolecente")
else:
    print("Es un adulto")

# Ejemplo de OR
if nEdad == 10 or nEdad == 20:
    print("Tengo una decena o dos docenas de años")
else:
    print("No tengo definicion")

# Ejemplo de NOT
if not nEdad == 10:
    print("Si tu edad es de 10 años")
else:
    print("No se tiene descripcion")

