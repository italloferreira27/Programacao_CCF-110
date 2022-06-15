import random
matrizA = [[0 for j in range(5)] for i in range(3)]
contsoma = 0
vetorsl = []

for i in range(3):
    for j in range(5):
        #matrizA[i][j] = int(input())
        matrizA[i][j] = random.randrange(0, 6)
        contsoma += matrizA[i][j]
    vetorsl.append(contsoma)
    contsoma = 0

for i in range(3):
    for j in range(5):
        print(f'{matrizA[i][j]}', end="  ")
    print(f'Soma da lina: {vetorsl[i]}')