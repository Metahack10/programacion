# condicion_if_true if condicion else condicion_if_false
Nombre = "Jorge"
Resultado = "Si es Jorge" if Nombre == "Jorge" else "No es Jorge"
print(Resultado)

Sexo = "M"
Resultado2 = ("Femenino","Masculino")[Sexo == "M"] # Otra forma de declarar un operador ternario
print(Resultado2)

Resultado3 = (5 < 6) or (3 > 10) # Otra forma de definir un operador ternario
print(Resultado3)
