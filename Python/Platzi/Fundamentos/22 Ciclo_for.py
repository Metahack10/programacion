"""
for element in range(1, 21):
    print(element)
"""
mi_lista = [23, 45, 67, 89, 43]
for element in mi_lista:
    print(element)

mi_tupla = ("nico", "jorge", "samuel")
for element in mi_tupla:
    print(element)

producto = {
    "nombre": "Camisa",
    "precio": 100,
    "stock": 89
}
for element in producto:
    print(element, "-->", producto[element])

for key, value in producto.items():
    print(key, "-->", value)

personas = [
    {
        "nombre":"jorge",
        "edad":42
    },
    {
        "nombre":"Juan",
        "edad": 30
    }
]
for persona in personas:
    print("nombre -->", persona["nombre"])