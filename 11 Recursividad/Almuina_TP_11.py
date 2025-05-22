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