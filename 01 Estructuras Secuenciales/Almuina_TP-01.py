# Ejercicio 1

print("hola mundo")

# Ejercico 2

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar_de_residencia = input("Ingresa tu pais de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

# Ejercicio 4

import math

radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# Ejercicio 5

cantidadDeSegundos = input("Ingrese la cantidad de segundos: ")
cantidadDeHoras = int(cantidadDeSegundos) // 3600
print(f"La cantidad de horas es: {cantidadDeHoras}")

# Ejercicio 6

numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
if num1 == 0 or num2 == 0:
    print("Error: Ambos números deben ser distintos de 0.")
else:
    suma = num1 + num2
    division = num1 / num2
    producto = num1 * num2
    resta = num1 - num2
    print(f"La suma de los números es: {suma}")
    print(f"La división de los números es: {division}")
    print(f"El producto de los números es: {producto}")
    print(f"La resta de los números es: {resta}")
    
# Ejercicio 8

altura = float(input("Ingrese la altura: "))
peso = float(input("Ingrese el peso: "))
imc = peso / altura**2
print(f"El IMC es: {imc:.2f}")

# Ejercicio 9

celcius = float(input("Ingrese la temperatura en grados Celcius: "))
fahrenheit = celcius * 9/5 + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

# Ejercicio 10

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números es: {promedio}")