multiplos_de_4 = [] # Lista que almacenará los múltiplos de 4

for i in range(1, 101): # Iterar del 1 al 100
    if i % 4 == 0: # Verificar si es múltiplo de 4
        multiplos_de_4.append(i) # Agregar a la lista

print("Los múltiplos de 4 entre 1 y 100 son:", multiplos_de_4) # Mostrar los múltiplos de 4