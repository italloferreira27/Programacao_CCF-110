import random
matriz = [[0 for j in range(5)] for i in range(7)]
for i in range(7):
    for j in range(5):
        #matriz[i][j] = int(input())
        matriz[i][j] = random.randrange(0, 10)
        if(matriz[i][j] % 2 != 0):
            matriz[i][j] = matriz[i][j] * 2

for i in range(7):
    for j in range(5):
        print(f'{matriz[i][j]}', end="  ")
    print()