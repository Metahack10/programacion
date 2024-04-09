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

#Metodos de escritura o modificacion para archivos
with open('D:/Development/programacion/Python/Platzi/Funciones y Errores/text.txt', 'w+') as file: #'r+' --> indica que abra el archivo con permisos de escritura y lectura, agregando el contenido a la ultima linea, mientras que w+ reemplaza el contenido en el archivo
    for line in file:
        print(line)
    file.write('nuevas cosas en este archivo\n')
    file.write("otra linea\n")
    file.write("mas linea")
