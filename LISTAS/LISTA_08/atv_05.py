import random
matriz = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        #matriz[i][j] = int(input())
        matriz[i][j] = random.randrange(0, 10)

#TESTANDO!!! NÃO PRECISA COPIAR
for i in range(10):
    for j in range(10):
        print(f'{matriz[i][j]}', end="  ")
    print()
print('\n')
#..............................

for i in range(10):
    for j in range(i+1, 10):
        print(f'{matriz[i][j]}', end="  ")
    print()
