conjunto_A = {"col", "mex", "bol"}
conjunto_B = {"pe", "bol"}

#Union --> Realiza la union de los elementos de 2 conjuntos, manteniendo valores unicos en el conjunto resultante
conjunto_C = conjunto_A.union(conjunto_B)
print(conjunto_C)
print(conjunto_A | conjunto_B)

#Intersection --> Devuelve un conjunto solo con elementos que se repiten tanto en A como en B
conjunto_C = conjunto_A.intersection(conjunto_B)
print(conjunto_C)
print(conjunto_A & conjunto_B)

#Difference --> Devuelve un conjunto con todos los elementos de A que no estan en B
conjunto_C = conjunto_A.difference(conjunto_B)
print(conjunto_C)
print(conjunto_A - conjunto_B)

#Symmetric_difference --> Devuelve la union de 2 conjunto sin los elementos de intercepción entre ambos
conjunto_C = conjunto_A.symmetric_difference(conjunto_B)
print(conjunto_C)
print(conjunto_A ^ conjunto_B)