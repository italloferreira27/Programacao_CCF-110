l = int(input('Linha: '))
c = int(input('Coluna: '))
matriz = [[0 for j in range(c)] for i in range(l)]
matrizTR = [[0 for j in range(l)] for i in range(c)]

for i in range(l):
    for j in range(c):
        matriz[i][j] = int(input())

print()
for i in range(l):
    for j in range(c):
        print(f'{matriz[i][j]}', end=" ")
    print()
print()

for i in range(c):
    for j in range(l):
        matrizTR[i][j] = matriz[j][i]

for i in range(c):
    for j in range(l):
        print(f'{matrizTR[i][j]}', end=" ")
    print()