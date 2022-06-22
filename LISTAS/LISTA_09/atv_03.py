n = 3 #10
matriz = [[0 for j in range(n)] for i in range(n)]
produto = 1
for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input())

for i in range(n):
    for j in range(n):
        print(f'{matriz[i][j]}', end=" ")
    print()    

for i in range(n):
    for j in range(i):
        produto *= matriz[i][j]

print(produto)