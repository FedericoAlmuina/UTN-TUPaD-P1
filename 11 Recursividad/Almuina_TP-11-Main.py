from Almuina_TP_11 import factorial, fibonacci, potencia
# Ejercicio 1

n = int(input("Ingrese un número entero no negativo: "))
print("El factorial de", n, "es:", factorial(n))

# Ejercicio 2

pos = int(input("Ingrese la posición de Fibonacci: "))
for i in range(pos + 1):
    print("Fibonacci en la posición", i, "es:", fibonacci(i))

# Ejercicio 3

exp = int(input("Ingrese el exponente: "))
base = int(input("Ingrese la base: "))
print("La potencia de", base, "elevado a", exp, "es:", potencia(base, exp))

# Ejercicio 4

