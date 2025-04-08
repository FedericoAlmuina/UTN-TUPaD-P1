#Ejercicio 1

# Slicitar la edad del usuario y determinar si es mayor o menor de edad
edad = int(input("Ingrese su edad: "))
# evaluar si la edad es mayor o menor de 18 años
if edad > 17:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

#Ejercicio 2

# Se solicita al usuario que ingrese su nota
nota = float(input("Ingrese su nota: "))
# Se evalua si la nota es esta entre 0 y 10
if nota < 0 or nota > 10:
    print("Nota inválida. Debe estar entre 0 y 10.")
# Evaluar si la nota es mayor o menor de 6
elif nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3

# Solicitamos un numero al usuario
numero = int(input("Ingrese un número: "))
# Evaluamos si el numero es par, impar o cero
# Si el numero es cero, mostramos un mensaje de error
if numero == 0:
    print("El número no puede ser cero.")
elif numero % 2 == 0:
    print("El número es par.")
else:
    print("Por favor, ingrese un número par.")

# Ejercicio 4

# Se solicita al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))
# Se evalua si la edad es negativa
# Si la edad es negativa, mostramos un mensaje de errorn luego evaluamos si la edad es menor a 12, entre 12 y 18, entre 18 y 30 o mayor a 30
if edad < 0:
    print("La edad no puede ser negativa.")
elif edad < 12:
    print("Niño/a.")
elif edad >= 12 and edad < 18:
    print("Adolescente.")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven.")
elif edad >= 30:
    print("Adulto/a.")
else:
    pass

# Ejercicio 5

#solicita a usuario que ingrese una contraseña
contraseña = input("Ingrese su contraseña: ")
# se evalua la longitud de la contraseña entre 8 y 14 caracteres
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Ejercicio 6

# Se importan las librerías necesarias
import random
from statistics import mode, median, mean
# Se generan 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Se calcula la moda, mediana y media de los números generados
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
# Se evalua el sesgo de los números generados
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo.")
elif media == mediana and mediana == moda:
    print("Sin sesgo.")
else:
    print("No se puede determinar el sesgo.")

# Ejercicio 7

# Solicitar una frase o palabra al usuario
texto = input("Ingresa una frase o palabra: ")
# Verificamos si la última letra es una vocal (minúscula o mayúscula) para ver si se añade un signo de exclamación
if texto[-1].lower() in "aeiou": 
    texto += "!"  # Añadir signo de exclamación
print("Resultado:", texto)

# Ejercicio 8

# solicitamos nombre al usuario y un numero del 1 al 3
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un número del 1 al 3: "))
# evaluamos si el numero es menor a 1 o mayor a 3
# Si el numero es menor a 1 o mayor a 3, mostramos un mensaje de error
if numero < 1 or numero > 3:
    print("Número inválido. Debe estar entre 1 y 3.")
elif numero == 1:
    nombre = nombre.upper() # si el numero es 1, convertimos el nombre a mayúsculas
elif numero == 2:
    nombre = nombre.lower() # si el numero es 2, convertimos el nombre a minúsculas
elif numero == 3:
    nombre = nombre.title() # si el numero es 3, convertimos la primera letra del nombre en mayuscula  
print (nombre)

# Ejercicio 9

# Se solicita al usuario que ingrese la magnitud de un terremoto en la escala Richter
magnitud = float(input("Ingrese la magnitud en escala Richter: "))
# Se evalua la magnitud y se muestra el mensaje correspondiente
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
else:
    print("Valor no válido. Por favor, ingrese un número válido.")

# Ejercicio 10

# Pedimos los datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Verificamos que el hemisferio sea válido
if hemisferio != "N" and hemisferio != "S":
    print("Hemisferio no válido. Usa 'N' o 'S'.")
else:
    # Determinar la estación según mes y día
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
    else:
        estacion = "Fecha no válida"

    print(f"Estás en {estacion}.")