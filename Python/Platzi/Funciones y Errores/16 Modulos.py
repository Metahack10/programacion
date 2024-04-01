import sys #Modulos de funciones y operaciones del sistema
print(sys.path)

import re #Modulo con funciones y procedimientos para expresiones regulares
text = "Mi numero de telefono es 76334743, el codigo de pais es 591, mi numero de la suerte es el 7"
result = re.findall("[0-9]+", text)
print(result)

import time #Modulo para trabajar con el tiempo y hora
timestamp = time.time()
print(timestamp)
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)
