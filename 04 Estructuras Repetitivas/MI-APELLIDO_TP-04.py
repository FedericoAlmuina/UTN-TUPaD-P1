# ejercicio 4

import math

# Función para calcular el área del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Solicitar el radio al usuario
radio = float(input("Ingresa el radio del círculo: "))

# Calcular área y perímetro usando las funciones
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Mostrar resultados
print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")

# Ejercicio 5

def segundos_a_horas(segundos):
    # Verificar si el número de segundos es válido
    if segundos < 1:
        # Si no es un número entero positivo, mostrar mensaje de error
        print("no ingreso una cantidad de segundos valida")
    else:
        # Convertir segundos a horas
        horas = segundos // 3600
        print(f"{segundos} segundos son {horas} hora/s.")

segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)

# Ejercicio 6

def tabla_multiplicar(numero):
    # Imprime la tabla de multiplicar del número dado
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar del 1 al 10: "))
tabla_multiplicar(numero)

# Ejercicio 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    print(f"El resultado de la suma es:{suma}\nEl resultado de la resta es: {resta}\nEl resultado de la multiplicacion es: {multiplicacion}\nEl resultado de la division es: {division}")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
operaciones_basicas(a, b)

# Ejercicio 8

def calcular_imc(peso, altura):
    # Verifica si el peso y la altura son válidos
    if peso <= 0 or altura <= 0:
        return "Peso y altura deben ser mayores que cero."
    # Calcula el IMC
    imc = peso / (altura ** 2)
    print(f"Tu IMC es {imc:.2f}")

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
calcular_imc(peso, altura)

# Ejercicio 9

def celsius_a_fahrenheit(celsius):
    print((celsius * 9/5) + 32)

celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

# Ejercicio 10

def caalcular_promedio(a, b, c):
    print((a + b + c) / 3)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
caalcular_promedio(a, b, c)