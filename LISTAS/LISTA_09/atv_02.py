n = 4 #10
matriz = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input())
        if(j == (n-1)-i):
            matriz[i][j] = 0

print(matriz)

for i in range(n):
    for j in range(n):
        if(matriz[i][j] != 0):
            print(matriz[i][j])

#COLOQUE esse uúltimoo print em um matriz e print a raiz