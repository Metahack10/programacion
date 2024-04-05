try:
    print(0 / 0)

    age = 10
    if age < 18:
        raise Exception("No se permiten menores de edad")
except ZeroDivisionError as error:
    print(error)
except Exception as error:
    print(error)

#print("Hola 3")

    assert 1 != 1, 'Uno no es diferente de uno'
except AssertionError as error:
    print(error)

print("Hola")
