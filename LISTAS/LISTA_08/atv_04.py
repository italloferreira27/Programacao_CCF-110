matriz = [[0 for j in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input())

for i in range(10):
    print(f'{matriz[i][i]}', end=' ')
