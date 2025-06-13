#Ejercicio 1

# Imprimir números del 0 al 100
for i in range(0, 101): # Inicializo en 0 y termino en 100, incrementando de 1 en 1
    print(i)

#Ejercicio 2

# Solicitar número al usuario
num = input("Ingresá un número entero: ")
# Verificar si es un número entero válido (positivo o negativo)
if num.lstrip('-').isdigit():
    # Convertir a entero
    numero = int(num)
    # Contar dígitos (sin contar el signo si es negativo)
    cantidad_digitos = len(num.lstrip('-'))
    print(f"El número tiene {cantidad_digitos} dígitos.")
else:
    print("No ingresaste un número entero válido.")

#Ejercicio 3

# Pedir los dos números al usuario 
a = int(input("Ingresá el primer número entero: "))
b = int(input("Ingresá el segundo número entero: "))
# Determinar el menor y el mayor para evitar errores
menor = min(a, b)
mayor = max(a, b)
# Sumar los números entre 'menor' y 'mayor', excluyéndolos
suma = 0
for i in range(menor + 1, mayor):
    suma += i
# Mostrar el resultado
print(f"La suma de los números entre {a} y {b}, excluyéndolos, es: {suma}")

# ejercicio 4

flag = True 
suma_total = 0
# Utilizo una bandera para controlar el bucle
while flag == True:
    entrada = input("Ingresá un número entero (0 para terminar): ")
    # Validar si es un número entero
    if entrada.lstrip('-').isdigit():
        numero = int(entrada)
        # Verificar si el número es 0 para salir del bucle
        if numero == 0:
            flag = False  # Salir del bucle si se ingresa 0
        else:
            suma_total += numero # Sumar el número a la suma total
    else:
        print("No es un número entero. Intentá de nuevo.")
        
if suma_total == 0: # Si no se ingresó ningún número
    print("No se ingresó ningún número.")
else:
    print(f"La suma total es: {suma_total}")

# ejercicio 5

import random

numero = random.randint(1, 9)  # Generar un número aleatorio entre 1 y 9
intentos = 0  # Inicializar el contador de intentos
flag = True   # Bandera para controlar el bucle

while flag:  # Bucle hasta que el usuario adivine el número
    entrada = int(input("Adiviná el número entero (1-9): "))
    intentos += 1  # Incrementar el contador de intentos
    if entrada == numero:
        flag = False  # Cambiar la bandera a False si el número es correcto

print(f"¡Felicidades! Adivinaste el número {numero} en {intentos} intentos.")

# ejercicio 6

for i in range(100, 0, -2): # incial en 100 y termina en 1, decrementando de 2 en 2
    print(i)

# ejercicio 7

numero = input("Ingresá un número entero positivo: ")
if numero.isdigit() and int(numero) > 0: # Verificar si es un número entero positivo
    numero = int(numero)
    suma = 0
    for i in range(1, numero + 1): # Sumar los números del 1 al número ingresado
        suma += i
    print(f"La suma de los números del 1 al {numero} es: {suma}")
else:
    print("No ingresaste un número entero positivo válido.")

# ejercicio 8

contador = 0
cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0
while contador < 100: # Bucle para ingresar 100 números
    numero = input("Ingresá un número entero: ")
    if numero.lstrip('-').isdigit(): # Verificar si es un número entero
        
        numero = int(numero)
        if numero % 2 == 0: # Verificar si es par
            cont_pares += 1
        else: # Si no es par, es impar
            cont_impares += 1
        if numero > 0: # Verificar si es positivo
            cont_positivos += 1
        elif numero < 0: # Verificar si es negativo
            cont_negativos += 1
    else: # Si no es un número entero, mostrar mensaje de error
        print("No es un número entero. Intentá de nuevo.")
        continue
    # Incrementar el contador de números ingresados
    contador += 1

# Mostrar los resultados
print(f"Cantidad de números pares: {cont_pares}")
print(f"Cantidad de números impares: {cont_impares}")
print(f"Cantidad de números positivos: {cont_positivos}")
print(f"Cantidad de números negativos: {cont_negativos}")
# Mostrar el total de números ingresados
print(f"Total de números ingresados: {contador}")

# ejercicio 9

contador = 0
suma = 0
while contador < 10: # Bucle para ingresar 100 números
    numero = input("Ingresá un número entero: ")
    if numero.lstrip('-').isdigit(): # Verificar si es un número entero
        
        numero = int(numero)
        suma += numero # Sumar el número ingresado
    else: # Si no es un número entero, mostrar mensaje de error
        print("No es un número entero. Intentá de nuevo.")
        continue
    # Incrementar el contador de números ingresados
    contador += 1
promedio = suma / contador # Calcular el promedio

print(f"El promedio de los {contador} números ingresados es: {promedio}")

# ejercicio 10

entrada = input("Ingresá un número entero: ")

# Validar que sea un número entero (permitir negativos)
while not entrada.lstrip('-').isdigit():
    print("Eso no es un número entero válido.")
    entrada = input("Intentá de nuevo: ")

# Invertir el número como string
if entrada[0] == '-':
    invertido = '-' + entrada[:0:-1]  # Invierte sin el signo
else:
    invertido = entrada[::-1]  # Inversión normal

print(f"Número invertido: {invertido}")