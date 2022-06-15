import random
matrizA = [[0 for j in range(4)] for i in range(4)]
matrizB = [[0 for j in range(4)] for i in range(4)]
matrizSOMA = [[0 for j in range(4)] for i in range(4)]

for i in range(4):
    for j in range(4):
        #matrizA[i][j] = int(input())
        #matrizB[i][j] = int(input())
        matrizA[i][j] = random.randrange(0, 6)
        matrizB[i][j] = random.randrange(0, 6)

#Copia nao↓
print('Tabela A:')
for i in range(4):
    for j in range(4):
        print(f'{matrizA[i][j]}', end="  ")
    print()
print() 

print('Tabela B:')
for i in range(4):
    for j in range(4):
        print(f'{matrizB[i][j]}', end="  ")
    print()
print()
#Copia  nao↑

for i in range(4):
    for j in range(4):
        matrizSOMA[i][j] = matrizA[i][j] + matrizB[i][j]

print('Tabela da soma de A e B:')
for i in range(4):
    for j in range(4):
        print(f'{matrizSOMA[i][j]}', end="  ")
    print()

