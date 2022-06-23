l = int(input('Linha: '))
c = int(input('Coluna: '))
matriz = [[0 for j in range(c)] for i in range(l)]
matrizTR = [[0 for j in range(c)] for i in range(l)] #Como é quadrada a ordem de l e c não importa
cont = 0

if(l == c):
    for i in range(l):
        for j in range(c):
            matriz[i][j] = int(input())
    print()

    print('MATRIZ NORMAL↓')
    for i in range(l):
        for j in range(c):
            print(matriz[i][j], end="  ")
        print()
    print()

    for i in range(l):
        for j in range(c):
            matrizTR[i][j] = matriz[j][i]

    print('MATRIZ TRANSPOSTA↓')
    for i in range(l):
        for j in range(c):
            print(matriz[i][j], end="  ")
        print()
    print()

    for i in range(l):
        for j in range(c):
            if(matrizTR[i][j] == matriz[i][j]):
                cont += 1
    
    if(cont == l*c):
        print('A matriz é SIMÉTRICA!!!')
    else:
        print('A matriz não é SIMÉTRICA!')

else:
    print('A MATRIZ NÃO É QUADRADA!')