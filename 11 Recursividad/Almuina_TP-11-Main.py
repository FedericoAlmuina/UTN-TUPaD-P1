from Almuina_TP_11 import factorial, fibonacci, potencia, decimal_a_binario, es_palindromo, suma_digitos, contar_bloques, contar_digito

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

numero = int(input("Introduce un número entero positivo: "))

if numero == 0: # Caso especial para el número 0
    print("0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")
# Ejercicio 5

texto = input("Introduce una palabra: ")
if es_palindromo(texto.lower()):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

# Ejercicio 6

num_ingresado = int(input("Ingrese un número entero positivo: "))
print("La suma de los dígitos de", num_ingresado, "es:", suma_digitos(num_ingresado))

# Ejercicio 7

numero_bloques = int(input("Ingrese el número de bloques: "))
print("El número total de bloques necesarios es:", contar_bloques(numero_bloques))


# Ejercicio 8

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")