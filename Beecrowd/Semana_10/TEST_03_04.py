import random
x = input()
matriz = [[0 for i in range(12)] for j in range(12)]
soma = 0
cont = 0

for i in range(6, 12):
    for j in range(12-i, i):
        #matriz[i].append(float(input()))
        matriz[i][j] = random.randrange(0, 100)
        soma += matriz[i][j]
        cont += 1

for i in range(12):
    for j in range(12):
        print(matriz[i][j], end=" ")
    print()

media = soma/cont
if(x == 'S'):
    print(soma)
elif(x == 'M'):
    print(f'{media:.1f}')
