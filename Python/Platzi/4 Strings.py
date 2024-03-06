name = "Jorge"
last_name = "Lopez Vicente"
print(name)
print(last_name)

#Concatenación de strings
full_name = name + " " + last_name
print(full_name)

#uso de la comilla en strings
quote = "I'm Jorge"
print(quote)
quote2 = 'She said "Hello"'
print(quote2)

#Format
template1 = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template1)
#Formato 2
template2 = "Hola, mi nombre es {} y mi apellido es {}".format(name,last_name)
print(template2)
#Formato 3
template3 = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template3)

#Reto
age = 42
template4 = f"Hola, mi nombre es {name} {last_name} y mi edad es {age}"
print(template4)
