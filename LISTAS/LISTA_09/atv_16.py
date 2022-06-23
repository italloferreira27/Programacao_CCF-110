#https://www.youtube.com/watch?v=kwVIZjSEZAk
matriz = [[0 for j in range(2)] for i in range(2)]
matriz_IN = [[0 for j in range(2)] for i in range(2)]
pdp = 1
pds = 1
dp = [0 for i in range(2)]
ds = [0 for i in range(2)]
for i in range(2):
    for j in range(2):
        matriz[i][j] = int(input())
 
for i in range(2):
    for j in range(i, i+1):
        pdp *= matriz[i][j]
    for j in range(1-i, 2-i):
        pds *= matriz[i][j]

determinante = pdp - pds

print('MATRIZ NORMAL↓')
for i in range(2):
    for j in range(2):
        print(matriz[i][j], end="  ")
    print()
print()

for i in range(2):
    for j in range(2):
        matriz[i][j] = matriz[i][j]/determinante

print('MATRIZ DEPOIS DE DIVIDIR PELO DETERMINANTE↓ ', determinante)
for i in range(2):
    for j in range(2):
        print(matriz[i][j], end="  ")
    print()
print()

for i in range(2):
    for j in range(i, i+1):
        dp[i] = matriz[i][j]
    for j in range(1-i, 2-i):
        ds[i] = matriz[i][j]*-1

for i in range(2):
    for j in range(2):
        if(i == j):
            matriz_IN[i][j] = dp[1-i]
        elif(j == 1-i):
            matriz_IN[i][j] = ds[i]

print('A matriz INVERSA↓')
for i in range(2):
    for j in range(2):
        print(matriz_IN[i][j], end="  ")
    print()
print()