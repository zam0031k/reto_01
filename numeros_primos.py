# Solicita la cantidad de números a analizar
while True:
    try:
        cantidad = int(input("Ingresa la cantidad de números que deseas analizar: "))
        break
    except ValueError:
        print("ERROR: ingresa una cantidad válida")

# Lista para almacenar los números ingresados
lista_numeros = []

# Solicita los números al usuario
while True:
    try:
        for i in range(cantidad):
            num = int(input(f"Digite el valor {i + 1}: "))
            lista_numeros.append(num)
        break
    except ValueError:
        print("ERROR: Valor NO numérico ingresado, por favor vuelve a intentarlo.")

def valores_primos(lista):
    """
    Encuentra y muestra los números primos de una lista dada.

    :param lista: Lista de números enteros.
    """
    primos = []
    for i in lista:
        if i > 1:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                primos.append(i)

    print("De los números mencionados, aquellos que son primos son:")
    for primo in primos:
        print(primo, end=" ")


# Llama a la función para analizar la lista de números
valores_primos(lista_numeros)
