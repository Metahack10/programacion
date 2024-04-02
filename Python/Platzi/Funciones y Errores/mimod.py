def get_poblacion():
    keys = ["col", "bol"]
    values = [300, 400]
    return keys, values

def poblacion_por_pais(data, pais):
    result = list(filter(lambda item: item["pais"] == pais, data))
    return result