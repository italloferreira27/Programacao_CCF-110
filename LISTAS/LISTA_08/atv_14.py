import random
matrizA = [[0 for j in range(10)] for i in range(5)]
maior = 0.0
guarda = []

for i in range(5):
    for j in range(10):
        #matrizA[i][j] = float(input())
        matrizA[i][j] = (round(random.uniform(0.00, 2.11), 2))
        if(matrizA[i][j] > maior):
            maior = matrizA[i][j]
    guarda.append(maior)
    maior = 0.0

#Copia nao↓
print('Altura dos jogadores:')
for i in range(5):
    for j in range(10):
        print(f'{matrizA[i][j]}', end='  ')
    print()
print()
#copia nao↑

for i in range(5):
    print(f'Maior da delegação {i}: {guarda[i]}')