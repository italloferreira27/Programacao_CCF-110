qnt = 2 #50
matriz = [[0 for j in range(3)] for i in range(qnt)]
precisa = 0

for i in range(qnt):
    for j in range(3):
        if(j == 0):
            matriz[i][j] = input('Nome: ')
        if(j == 1):
            matriz[i][j] = int(input('Ideal: '))
        if(j == 2):
            matriz[i][j] = int(input('Estoque: '))

for i in range(qnt):
#    for j in range(3):
        if(matriz[i][1] > matriz[i][2]):
            precisa = matriz[i][1] - matriz[i][2]
            print(f'A {matriz[i][0]} vai precisar de {precisa} plantas.')
        else:
            print(f'A {matriz[i][0]} está com o estoque suficiente.')