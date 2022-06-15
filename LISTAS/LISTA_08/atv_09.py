import random
matriz = [[0 for j in range(4)] for i in range(3)]
for i in range(3):
    for j in range(4):
        #matriz[i][j] = int(input())
        matriz[i][j] = random.randrange(0, 10)

#Copia nao ↓
for i in range(3):
    for j in range(4):
        print(f'{matriz[i][j]}', end='  ')
    print()
print()
#Copia nao ↑

print('O triplo da tabela 1')
for i in range(3):
    for j in range(4):
        print(f'{matriz[i][j]*3}', end='  ')
    print()