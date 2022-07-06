x = input()
matriz = [[0 for i in range(12)] for j in range(12)]
soma = 0
cont = 0

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

        
for i in range(7, 12):
    for j in range(11-i, 11-i):
        soma += matriz[i][j]
        cont += 1

media = soma/cont
if(x == 'S'):
    print(f'{soma:.1f}')
elif(x == 'M'):
    print(f'{media:.1f}')