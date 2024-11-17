# Desarrollo del reto_01

## Ejercicio 1: Calculadora básica

## Descripción:
Este ejercicio consiste en realizar una operación matemática entre dos números según un operador proporcionado por el usuario. 

## Solución: 
- Se solicitó al usuario ingresar dos números y un operador.
- Se utilizó la estructura `match-case` para seleccionar el operador adecuado y realizar la operación correspondiente.
- Se gestionaron los casos de división por cero y entrada de operadores no válidos.

## Ejercicio 2: Palíndromos

### Descripción:
Este ejercicio consiste en verificar si una palabra ingresada por el usuario es un palíndromo, es decir, que se lee igual de izquierda a derecha que de derecha a izquierda.

### Solución: 
- La palabra se convirtió en una lista de caracteres.
- La lista se invirtió y se comparó con la original para verificar si era un palíndromo.

## Ejercicio 3: Números primos
### Descripción:
Este ejercicio consiste en identificar números primos dentro de una lista de números proporcionada por el usuario.

### Solución: 
- Se solicitó al usuario una lista de números y luego se verificó si cada número era primo.
- El algoritmo de verificación comprueba que el número solo sea divisible por 1 y por sí mismo al sacar el modulo de la división que hay entre el rango de dos y la raíz del mismo.

## Ejercicio 4: Palabras con los mismos caracteres
### Descripción:
Este ejercicio consiste en encontrar palabras que tienen los mismos caracteres, aunque en diferente orden.

## Solución: 
- Se verificó si las palabras en la lista, al ser ordenadas con el método `sorted` coincidian entre sí.

## Ejercicio 5: Mayor suma de elementos consecutivos
### Descripción:
En este ejercicio, se solicita una lista de números y se encuentra la mayor suma de dos elementos consecutivos en la lista.

## Solución: 
- Se iteró sobre la lista y se calculó la suma de elementos consecutivos, manteniendo en una variable la mayor suma encontrada.
