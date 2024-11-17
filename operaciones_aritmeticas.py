def calcular(numero1, numero2, operador):
    """
    Realiza una operación matemática entre dos números según el operador.

    :param numero1: El primer número.
    :param numero2: El segundo número.
    :param operador: El operador a usar para la operación ('+', '-', '*', '/').
    :return: El resultado de la operación.
    """
    match operador:  # Se usa match-case para determinar el operador.
        case '+':  
            resultado = numero1 + numero2
        case '-': 
            resultado = numero1 - numero2
        case '*':  
            resultado = numero1 * numero2
        case '/':  
            if numero2 == 0:
                print('ERROR, no se puede dividir entre cero')
                return  # Termina la función si el divisor es cero.
            else:
                resultado = numero1 / numero2
        case _:  # Caso por defecto si el operador no es válido.
            print('ERROR, operador no reconocido. Por favor vuelva a intentarlo')
            return  # Termina la función si el operador es inválido.

    print(f'El resultado de la operación {numero1} {operador} {numero2} es: {resultado}')

while True:
    try:
        numero1 = int(input('Ingresa el primer valor: '))  # Solicita el primer número.
        operador = input('Ingresa el carácter del operador: ')  # Solicita el operador.
        numero2 = int(input('Ingresa el segundo valor: '))  # Solicita el segundo número.
        break

    except ValueError:
        print('ERROR, parece que has ingresado un valor NO numérico. favor vuelve a intentarlo')
        

calcular(numero1, numero2, operador)  # Llama a la función calcular.
