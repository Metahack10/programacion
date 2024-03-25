text = "Ella sabe Python"
print(text[0]) #[] se utiliza para colocar el indice o posición del caracter que se desea imprimir, las posiciones empiezan del 0
print(text[1])
size = len(text)
print(text[size-1]) # Se imprime el ultimo caracter de la cadena
print(text[len(text)-1])
print(text[-1]) # Imprime el caracter que esta en la ultima posición de la cadena
print(text[-2]) # Imprime el caracter que esta en la penultima posición de la cadena

# slicing
print(text[0:5]) #Imprime los caracteres indicados desde el inicio hasta el fin indicado 0:5 --> del 0 al 5
print(text[10:16])
print(text[:10]) #Del 0 al 10, cuando no se especifica toma por defecto la posicion 0
print(text[5:-1]) #No toma en cuenta el ultimo caracter, va de 5 al penultimo caracter de la cadena
print(text[5:]) # Si no se especifica el punto final, se toma por defecto la posicion final de la cadena (5:) va de 5 al final de la cadena
print(text[:]) #Imprime desde la posicion inicial a la posicion final de la cadena
print(text[10:16:1]) #Imprime los caracteres indicados en el rango de inicio a fin, saltando un espacio o posicion
print(text[10:16:2]) #Imprime los caracteres indicados en el rango de inicio a fin, saltando dos espacios o posiciones
print(text[::2]) #Imprime los caracteres desde el inicio hasta el final, saltando de a dos espacios o posiciones
print(text[::-1]) #Imprime los caracteres desde el final al inicio, saltando de a un espacio o posicion






