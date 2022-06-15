import random
matriz = [[0 for j in range(5)] for i in range(4)]
soma = 0
for i in range(4):
    for j in range(5):
        #matriz[i][j] = int(input())
        matriz[i][j] = random.randrange(0, 6)
        soma += matriz[i][j]

#Copia nao↓
print('Tabela A:')
for i in range(4):
    for j in range(5):
        print(f'{matriz[i][j]}', end='  ')
    print()
print()
#Copia nao↑

print(f'Soma da Tabela A: {soma}')
