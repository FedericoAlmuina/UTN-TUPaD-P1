#ejercicio 1

multiplos_de_4 = [] # Lista que almacenará los múltiplos de 4

for i in range(1, 101): # Iterar del 1 al 100
    if i % 4 == 0: # Verificar si es múltiplo de 4
        multiplos_de_4.append(i) # Agregar a la lista

print("Los múltiplos de 4 entre 1 y 100 son:", multiplos_de_4) # Mostrar los múltiplos de 4

# ejercicio 2

cosas = ["naranja", "perro", "gato", "computadora", "trabajo"] # Lista que almacenará las cosas
print("El pénultimo elemento de la lista es:", cosas[-2]) # Mostrar el último elemento de la lista

# ejercicio 3

lista_vacia = []

lista_vacia.append("Quilmes") # Agregar elementos a la lista vacía
lista_vacia.append("Atletico") # Agregar elementos a la lista
lista_vacia.append("Club") # Agregar elementos a la lista

print(lista_vacia) # Mostrar la lista vacía

# ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]

animales[-3] = "loro"  # Cambiar el segundo elemento de la lista
animales[-1] = "oso"  # Cambiar el cuarto elemento de la lista

print(animales)

# ejercicio 5

""" Lo que hace el siguiente código es eliminar el numero mas grande de la lista """
numeros = [ 8 , 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# ejercicio 6

numeros_de_10_al_30 = []
for i in range(10, 31 , 5):
    numeros_de_10_al_30.append(i) # Agregar elementos a la lista de 10 a 30 de 5 en 5
print(numeros_de_10_al_30[0:2]) # mostrar los dos primeros elementos de la lista

# ejercicio 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = ["bora", "vento"] # Cambiar el segundo y tercer elemento de la lista

print(autos)

# ejercicio 8

dobles = []
for i in range(5, 16, 5):
    dobles.append(i * 2) # Agregar elementos a la lista el doble de 5, 10 y 15
print(dobles)

# ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")  # Agregar "jugo" a la lista de compras del 3ro
compras[1][1] = "tallarines" # Cambiar "fideos" por "tallarines" en la lista de compras del 2do
compras[0].remove("pan") # Eliminar "pan" de la lista de compras del 1ro

print(compras)

# ejercicio 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)