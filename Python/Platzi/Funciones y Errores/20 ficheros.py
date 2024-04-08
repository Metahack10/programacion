file = open('D:/Development/programacion/Python/Platzi/Funciones y Errores/text.txt')
#print(file.read())
"""
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
"""

for line in file:
    print(line)

file.close()

with open('D:/Development/programacion/Python/Platzi/Funciones y Errores/text.txt') as file:
    for line in file:
        print(line)
