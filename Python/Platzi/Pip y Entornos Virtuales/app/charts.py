import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f"Python/Platzi/Pip y Entornos Virtuales/app/imgs/{name}.png")
    plt.close()

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.savefig("Python/Platzi/Pip y Entornos Virtuales/app/imgs/pie.png")
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    generate_pie_chart(labels, values)