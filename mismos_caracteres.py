# Solicita la cantidad de palabras a analizar
while True:
    try:
        cantidad_palabras = int(input("Ingresa la cantidad de palabras que deseas analizar: "))
        break
    except ValueError:
        print("ERROR: ingresa una cantidad válida")

# Lista para almacenar las palabras
lista_palabras = []

# Solicita las palabras y las agrega a la lista
for i in range(cantidad_palabras):
    palabra = input(f'Ingresa la palabra {i + 1}: ')
    lista_palabras.append(palabra)


# Función que encuentra palabras con los mismos caracteres
def analizar_caracteres(lista):
    """
    Analiza la lista de palabras y retorna aquellas que tienen los mismos caracteres.

    :param lista: Lista de palabras a analizar.
    :return: imprime las palabras que comparten los mismos caracteres.
    """
    lista_mismos_caracteres = []
    
    for i in lista:
        for j in lista:
            if i == j or i in lista_mismos_caracteres:
                continue
            if sorted(i) == sorted(j):
                lista_mismos_caracteres.append(i)
                lista_mismos_caracteres.append(j)
    
    # Si no hay coincidencias, muestra mensaje
    if not lista_mismos_caracteres:
        print('No existen elementos que comparten los mismos caracteres')
        return ''
    
    # Muestra las palabras que coinciden
    print(f'Los elementos que comparten los mismos caracteres son: {lista_mismos_caracteres}')


# Llama a la función con la lista de palabras
analizar_caracteres(lista_palabras)
