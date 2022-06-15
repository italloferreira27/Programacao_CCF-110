operacao = input()
matriz = [[0 for i in range(12)] for i in range(12)]
soma = 0
media = 0
conta = 0

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

if(operacao == 'S'):
    for i in range(6):
        for j in range(12-i, 12):
            soma += matriz[i][j]
    for i in range(6, 12):
        for j in range(i+1,12):
            soma += matriz[i][j]
    print(f"{soma:.1f}")

if(operacao == 'M'):
    for i in range(6):
        for j in range(12-i, 12):
            soma += matriz[i][j]
            conta += 1
    for i in range(6, 12):
        for j in range(i+1, 12):
            soma += matriz[i][j]
            conta += 1
    media = soma/conta
    print(f"{media:.1f}")