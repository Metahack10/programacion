import mimod

data = [
    {
        "pais":"Colombia",
        "poblacion": 500
    },
    {
        "pais":"Bolivia",
        "poblacion": 300
    }
]

def run():
    keys, values = mimod.get_poblacion()
    print(keys,values)

    pais = input("Digite el Pais que desea filtrar: ")
    result = mimod.poblacion_por_pais(data,pais)
    print(result)

if __name__ == "__main__":
    run()