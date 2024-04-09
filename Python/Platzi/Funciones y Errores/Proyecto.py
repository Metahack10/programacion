import csv
import mimod
import matplotlib.pyplot as plt

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        #print(header)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()

if __name__=="__main__":
    data = read_csv("D:/Development/programacion/Python/Platzi/Funciones y Errores/data.csv")
    #print(data)
    data = list(filter(lambda item: item["Continent"] == "South America", data))
    paises = list(map(lambda x: x["Country/Territory"], data))
    porcentajes = list(map(lambda x : x["World Population Percentage"], data))
    generate_pie_chart(paises, porcentajes)
    
    """
    pais = input("Seleccione el pais que desea graficar su poblacion: ")
    result = mimod.poblacion_por_pais(data, pais)

    if len(result) > 0:
        pais = result[0]
        labels, values = mimod.get_poblacion(pais)
        generate_bar_chart(labels, values)
    """
