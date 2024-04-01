items = [
    {
        "Product":"camisa",
        "Precio":100
    },
    {
        "Product":"pantalones",
        "Precio":300
    },
    {
        "Product":"short",
        "Precio":200
    }
]

precios = list(map(lambda item: item["Precio"], items))
print(precios)

def add_taxes(item):
    new_item = item.copy() #Genera una copia del item para dejar de compartir la referencia de memoria del diccionario original para evitar su cambio
    new_item["Tax"] = new_item["Precio"] * .19
    return new_item

new_items = list(map(add_taxes,items))
print(items)
print(new_items)
