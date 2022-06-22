import random
qnt = 10
matriz = [[0 for j in range(qnt)] for i in range(qnt)]

for i in range(qnt):
    for j in range(qnt):
        matriz[i][j] = random.randrange(0, 10)

for i in range(qnt):
    for j in range(qnt):
        print(f'{matriz[i][j]}', end="  ")
    print()
print()

#Trocando 2 pela 8 LINHA
for j in range(qnt):
    matriz[1][j], matriz[7][j] = matriz[7][j], matriz[1][j]

print('Trocando 2 pela 8 LINHA')
for i in range(qnt):
    for j in range(qnt):
        print(f'{matriz[i][j]}', end="  ")
    print()
print()

#Trocando 4 pela 10 COLUNA
for i in range(qnt):
    matriz[i][3], matriz[i][9] = matriz[i][9], matriz[i][3]

print('Trocando 4 pela 10 COLUNA')
for i in range(qnt):
    for j in range(qnt):
        print(f'{matriz[i][j]}', end="  ")
    print()
print()

#Trocando Diagonal principal pela Diagonal Secundaria
for i in range(0, 5):
    for j in range(0, 5):
        dp = matriz[i][j]
        matriz[i][j] = matriz[i][9-j]
        matriz[i][9-j] = dp

#Trocando Diagonal principal pela Diagonal Secundaria
for i in range(5, 10):
    for j in range(4, -1, -1):
        ds = matriz[i][j]
        matriz[i][j] = matriz[i][9-j]
        matriz[i][9-j] = ds



print('Trocando Diagonal principal pela Diagonal Secundaria')

#Matriz com os valors tocados
for i in range(qnt):
    for j in range(qnt):
        print(f'{matriz[i][j]}', end="  ")
    print()