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
    print("\n--- Consulta de contactos ---")
    consulta = input("Ingresa un nombre para buscar (o 'salir' para terminar): ")
    
    if consulta.lower() == 'salir':
        print("¡Hasta luego!")
        continuar = False  # Cambiamos la variable para salir del bucle
    else:
        if consulta in contactos:
            print(f"El número de {consulta} es: {contactos[consulta]}")
        else:
            print(f"Lo siento, {consulta} no está en la agenda.")