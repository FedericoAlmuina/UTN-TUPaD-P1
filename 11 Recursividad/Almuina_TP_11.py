# Ejercicio 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejercicio 2

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Ejercicio 3

def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)

# Ejercicio 4

def decimal_a_binario(n):
    if n == 0:
        return "" # Caso base: si n es 0, devuelve una cadena vacía
    else:
        return decimal_a_binario(n // 2) + str(n % 2) #Divide entre 2 y concatena el resto como un string

# Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1: # Caso base: si la palabra tiene 0 o 1 letras, es un palíndromo
        return True
    if palabra[0] != palabra[-1]: # Comparar primera y última letra
        return False
    return es_palindromo(palabra[1:-1]) # Llamada recursiva con la subcadena sin la primera y última letra

# Ejercicio 6

def suma_digitos(n):
    if n < 10: # Caso base: si n es menor a 10, ya es un solo dígito
        return n
    return (n % 10) + suma_digitos(n // 10) # Separar el último dígito y sumar recursivamente el resto

# Ejercicio 7

def contar_bloques(n):
    if n == 1: # Caso base: cuando n es 1, solo se necesita un bloque
        return 1 # Paso recursivo: sumar los bloques del nivel actual con los del nivel superior
    return n + contar_bloques(n - 1)

# Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0: # Caso base: si el número es 0, no hay más dígitos para analizar
        return 0
    if numero % 10 == digito: # Verificamos si el último dígito del número coincide con el dígito buscado
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)