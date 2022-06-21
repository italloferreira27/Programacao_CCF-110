x = int(input())
operacao = input()
soma = 0.0
media = 0.0
matriz = [[0 for i in range(12)] for j in range(12)]#12
for i in range(12):#12
    for j in range(12):#12
        matriz[i][j] = float(input())

if(operacao == 'S'):
    for i in range(12):#12
        soma += matriz[x][i]
    print(f"{soma:.1f}")

if(operacao == 'M'):
    for i in range(12):#12
        soma += matriz[x][i]
    media = soma/12
    print(f"{media:.1f}")
