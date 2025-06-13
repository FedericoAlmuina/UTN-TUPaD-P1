N = 5  
A = [0] * N  
B = [0] * N  

for i in range(N):  
    A[i] = i + i + i  # A = [0, 3, 6, 9, 12]

for i in range(N):  
    B[i] = i * 2  # B = [0, 2, 4, 6, 8]

contador = 0  
for i in range(N):  
    if A[0] < A[i] and A[i] == B[i]:  # solo 1 vez se cumple
        contador += 1  
        N = N - contador  

resultado = str(contador)  # resultado = "1"

if A[0] == 1:  # A[0] = 0 → falso
    resultado = "VERDADERO"  
elif A[0] == 2:  # falso
    resultado = "2"  
elif A[0] == 3:  # falso
    resultado = "FALSO"  

print(resultado)