# Solicita una palabra al usuario
palabra = input('Escribe una palabra: ')

# Inicializa las listas para la palabra y su inversa
lista_palabra = []
palabra_invertida = []

# Convertir la palabra en una lista de caracteres
for i in palabra:
    lista_palabra.append(i)
    palabra_invertida.append(i)

# Invertir la lista palabra_invertida
palabra_invertida.reverse()

def verificar_palindromo(lista_palabra, palabra_invertida):
    """
    Verifica si la palabra proporcionada es un palíndromo.

    :param lista_palabra: Lista de caracteres de la palabra original.
    :param palabra_invertida: Lista de caracteres de la palabra invertida.
    """
    if lista_palabra == palabra_invertida:
        print(f'La palabra proporcionada "{palabra}", efectivamente corresponde a un palíndromo.')
    else:
        print(f'La palabra proporcionada "{palabra}", NO corresponde a un palíndromo.')

# Llamada a la función para verificar si la palabra es un palíndromo
verificar_palindromo(lista_palabra, palabra_invertida)
