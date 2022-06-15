import random
matriz = [[0 for j in range(4)] for i in range(12)]
somames = 0
somaano = 0
contames = []

for i in range(12):
    for j in range(4):
        #matriz[i][j] = float(input())
        matriz[i][j] = (round(random.uniform(100.00, 1000.00), 2))
        somaano += matriz[i][j]
        somames += matriz[i][j]
    contames.append(somames)
    somames = 0

#Copia nao↓
print('Tabela dos valores recebidos:')
for i in range(12):
    for j in range(4):
        print(f'{matriz[i][j]}', end='  ')
    print()
print()
#copia nao↑

print(f'Total vendido em cada mês:')
for i in range(12):
    print(f"Mês {i+1} R${contames[i]:.2f}")
print()

print('Total recebido em cada semana:')
for i in range(12):
    for j in range(4):
        print(f'R$ {matriz[i][j]}', end='  ')
    print()
print()

print(f'Total recebido no ano: {somaano:.2f}')