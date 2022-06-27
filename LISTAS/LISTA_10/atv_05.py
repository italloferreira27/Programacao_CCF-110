n = int(input('Digite a quantidade de carros: '))
matriz = [[0 for j in range(2)] for i in range(n)]

for i in range(n):
    for j in range(2):
        matriz[i][j] = input()

for i in range(n):
    for j in range(1, 2):
        matriz[i][j] = int(matriz[i][j])

maior = matriz[0][1]
nome = matriz[0][0]
for i in range(n):
    for k in range(i+1, n):
            if(matriz[k][1] > matriz[i][1]):
                maior = matriz[i][1]
                matriz[i][1] = matriz[k][1]
                matriz[k][1] = maior
                nome = matriz[i][0]
                matriz[i][0] = matriz[k][0]
                matriz[k][0] = nome
#...........CONFERINDO...................
print()
for i in range(n):
    for j in range(2):
        print(matriz[i][j], end=" ")
    print()
print()
#.........................................

print(f'O carro {matriz[0][0]} é o mais econômico, fazendo {matriz[0][1]} Km/l.\n')

for i in range(n):
    print(f'O carro {matriz[i][0]} gasta R${(1000/matriz[i][1])*3.5:.2f} para percorrer 1000km.')