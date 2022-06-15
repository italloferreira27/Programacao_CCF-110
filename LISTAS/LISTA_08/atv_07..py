import random
matriz = [[0 for j in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        #matriz[i][j] = int(input())
        matriz[i][j] = random.randrange(0, 10)

#TESTANDO!!! NÃO PRECISA COPIAR
for i in range(10):
    for j in range(10):
        print(f'{matriz[i][j]}', end="  ")
    print()
print()
#...............................

for i in range(0, 10, 1):
    matriz.remove(matriz[i][9-i])
    
for i in range(9):
    for j in range(9):
        print(f'{matriz[i][j]}', end="  ")
    print()
