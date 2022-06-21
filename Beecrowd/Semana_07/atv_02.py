matriz = [[0 for i in range(12)] for j in range(12)]
operacao = input()
soma = 0
conta = 0
media = 0 
for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())
if(operacao == 'S'):
    for i in range(12):
        for j in range(i+1, 12):
            soma += matriz[i][j]
    print(f"{soma:.1f}")

if(operacao == 'M'):
    for i in range(12):
        for j in range(i+1, 12):
            soma += matriz[i][j]
            conta += 1
    media = soma/conta
    print(f"{media:.1f}")