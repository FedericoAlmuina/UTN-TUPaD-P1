# Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})  # Agregar varios elementos a la vez
precios_frutas['Naranja'] = 1200  # Agregar naranja
precios_frutas['Manzana'] = 1500  # Agregar manzana
precios_frutas['Pera'] = 2300  # Agregar pera

print(precios_frutas)

# Ejercicio 2

precios_frutas['Banana'] = 1330  # Actualizar el precio de la banana
precios_frutas['Manzana'] = 1700  # Actualizar el precio de la manzana
precios_frutas['Melón'] = 2800  # Actualizar el precio del melón

print(precios_frutas)

# Ejercicio 3

print(precios_frutas.keys())  # Imprimir solo las frutas

# Ejercicio 4

contactos = {} # Crear un diccionario vacío para almacenar contactos

for i in range(5): # Solicitar 5 contactos
    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    numero = input(f"Ingresa el número de teléfono para {nombre}: ")
    contactos[nombre] = numero

continuar = True
while continuar:
    consulta = input("Ingresa un nombre para buscar (o 'salir' para terminar): ")
    
    if consulta.lower() == 'salir':
        print("¡Hasta luego!")
        continuar = False  # Cambiamos la variable para salir del bucle
    else:
        if consulta in contactos:
            print(f"El número de {consulta} es: {contactos[consulta]}")
        else:
            print(f"Lo siento, {consulta} no está en la agenda.")
# Ejercicio 5

frase = input("Ingrese una frase: ")

frase_dividida = frase.lower().split()# Dividir la frase en palabras

palabras_unicas = set(frase_dividida)  # Crear un conjunto para almacenar las palabras únicas
print(palabras_unicas)  # Imprimir las palabras únicas

conteo_palabras = {}
for palabra in frase_dividida:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1  # Contar la frecuencia de cada palabra

print(conteo_palabras)

# Ejercicio 6

alumnos = {}

# Solicitar datos para 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} para {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)  # Guardamos como tupla

# Calcular y mostrar promedios
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")  # Mostramos con 2 decimales

# Ejercicio 7

# Definimos los sets de estudiantes (ejemplo)
parcial1 = {"Federico", "Camila", "Carlos", "Brenda", "Milton"}
parcial2 = {"Brenda", "Messi", "Federico", "Sofía", "Milton"}

# 1. Estudiantes que aprobaron ambos parciales (intersección)
aprobados_ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", aprobados_ambos)

# 2. Estudiantes que aprobaron solo uno (diferencia simétrica)
aprobados_solo_uno = parcial1 ^ parcial2
print("\nAprobaron solo un parcial:", aprobados_solo_uno)

# 3. Lista total de aprobados en al menos un parcial (unión)
total_aprobados = parcial1 | parcial2
print("\nTotal de aprobados en al menos un parcial:", total_aprobados)

# Ejercicio 8

# Diccionario inicial con productos y su stock
stock_productos = {
    "manzanas": 10,
    "naranjas": 8,
    "bananas": 15
}

# Mostrar el stock actual
print("Stock actual:", stock_productos)

# Pedir al usuario un producto
producto = input("Ingresá el nombre del producto: ").lower()

# Consultar el stock
if producto in stock_productos:
    print(f"El stock de '{producto}' es: {stock_productos[producto]} unidades.")
    
    # Preguntar si quiere agregar unidades
    agregar = input("¿Querés agregar unidades? (sí/no): ").lower()
    if agregar == "sí" or agregar == "si":
        try:
            cantidad = int(input("¿Cuántas unidades querés agregar?: "))
            stock_productos[producto] += cantidad
            print(f"Nuevo stock de '{producto}': {stock_productos[producto]} unidades.")
        except ValueError:
            print("Por favor ingresá un número válido.")
else:
    print(f"'{producto}' no existe en el inventario.")
    agregar_nuevo = input("¿Querés agregar este nuevo producto? (sí/no): ").lower()
    if agregar_nuevo == "sí" or agregar_nuevo == "si":
        try:
            cantidad = int(input("¿Cuántas unidades tiene?: "))
            stock_productos[producto] = cantidad
            print(f"'{producto}' fue agregado con {cantidad} unidades.")
        except ValueError:
            print("Por favor ingresá un número válido.")

# Mostrar el stock actualizado
print("Stock actualizado:", stock_productos)

# Ejercicio 9

# Definimos la agenda con tuplas (día, hora) como claves
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("lunes", "15:00"): "Clase de programación",
    ("martes", "09:00"): "Revisión de proyectos",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Cita médica",
    ("jueves", "14:00"): "Almuerzo con cliente"
}

def consultar_agenda():
    #Consulta qué evento hay en un día y hora específicos
    print("\n--- CONSULTA DE AGENDA ---")
    dia = input("Ingrese el día (ej: lunes): ").lower()
    hora = input("Ingrese la hora (formato HH:MM): ")
    
    # Buscamos el evento en la agenda
    evento = agenda.get((dia, hora), "No hay eventos programados")
    
    print(f"\nEl {dia} a las {hora}: {evento}")

# Función para mostrar toda la agenda
def mostrar_agenda_completa():
    print("\n--- AGENDA COMPLETA ---")
    for (dia, hora), evento in agenda.items():
        print(f"El {dia} a las {hora}: {evento}")

# Menú principal
while True:
    print("\nOPCIONES:")
    print("1. Consultar evento")
    print("2. Ver agenda completa")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        consultar_agenda()
    elif opcion == "2":
        mostrar_agenda_completa()
    elif opcion == "3":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

# Ejercicio 10

# Diccionario original (país: capital)
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

# Invertir el diccionario (capital: país)
invertido = {capital: pais for pais, capital in original.items()}

# Mostrar resultados
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)
