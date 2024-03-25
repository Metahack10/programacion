x = 3.3
y = 1.1 + 2.2
print(x)
print(y)
print(x == y)

#Metodo 1: Comparando flotantes (string)
y_str = format(y,".2g")
print("str ->",y_str)
print(y_str == str(x))

#Metodo 2: Comparando flotantes (matematica)
tolerancia = 0.00001
print(abs(x - y) < tolerancia)
