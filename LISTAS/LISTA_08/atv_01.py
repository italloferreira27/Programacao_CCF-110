matriz = [[0 for j in range(5)] for i in range(5)]

for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input())

print('AS ÚLTIMAS POSIÇÕES SÃO ↓↓↓')
for i in range(5):
    print(f'{matriz[i][4]}')