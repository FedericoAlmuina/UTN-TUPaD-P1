# Entrada de datos
dia = int(input("Introduce el valor N°1: "))  # 6
mes = int(input("Introduce el valor N°2: "))  # 2
anio = int(input("Introduce el valor N°3: "))  # 7

if mes in [1, 3, 5, 7, 8, 10, 12]:  # Primer ⬜ reemplazado por "in"
    dd = 31
elif mes in [4, 6, 9, 11]:  # Segundo ⬜ reemplazado por "in"
    dd = 30
elif mes == 2:  # Tercer ⬜ reemplazado por "=="
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dd = 29
    else:
        dd = 28
else:
    print("A")
    dd = -1

if dd != -1:  # Cuarto ⬜ reemplazado por "!="
    if dia < 1 or dia > dd:
        print("B")
    elif mes < 1 or mes > 12:
        print("C")
    else:
        print("D")  # Salida esperada: "D"