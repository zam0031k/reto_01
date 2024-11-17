# Solicita la cantidad de números a incluir en la lista
while True:
    try:
        cantidad = int(input("Define la cantidad de números que desea tener en su lista: "))
        break
    except ValueError:
        print("ERROR: Ingresa una cantidad válida.")

# Lista para almacenar los números ingresados
lista_numeros = []

# Solicita los valores para la lista
while True:
    try:
        for i in range(cantidad):
            valor = int(input(f"Ingresa el valor {i + 1}: "))
            lista_numeros.append(valor)
        break
    except ValueError:
        print("ERROR: Valor NO numérico ingresado, por favor vuelve a intentarlo.")


def mayor_suma_elementos(lista):
    """
    Encuentra la mayor suma de elementos consecutivos en una lista.
    
    :param lista: Lista de números enteros.
    """
    mayor_suma = 0
    valor1 = 0
    valor2 = 0

    for i in range(len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if mayor_suma < suma_actual:
            mayor_suma = suma_actual
            valor1 = lista[i]
            valor2 = lista[i + 1]

    print(f"La suma entre los elementos consecutivos {valor1} y {valor2} da el mayor resultado: {mayor_suma}")


# Llama a la función para calcular la mayor suma de elementos consecutivos
mayor_suma_elementos(lista_numeros)
