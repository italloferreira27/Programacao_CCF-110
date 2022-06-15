matriz = [[0 for j in range(7)] for i in range(7)]
n = int(input())
cont = 0

for i in range(7):
    for j in range(7):
        matriz[i][j] = int(input())

for i in range(7):
    for j in range(7):
        if(matriz[i][j] == n):
            print(f'O valor {n} encontra-se na linha {i} e na coluna {j}.')
            cont += 1

if(cont == 0):
    print('ERRO! Esse valor não existe nessa matriz.')
            