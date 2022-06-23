l = int(input('Linha: '))
c = int(input('Coluna: '))
matriz = [[0 for j in range(c)] for i in range(l)]
matriz_TR = [[0 for j in range(c)] for i in range(l)] #Como é quadrada a ordem de l e c não importa
matriz_OP = [[0 for j in range(c)] for i in range(l)] #Como é quadrada a ordem de l e c não importa
cont = 0

if(l == c):
    for i in range(l):
        for j in range(c):
            matriz[i][j] = int(input())
    
    print('MATRIZ NORMAL↓')
    for i in range(l):
        for j in range(c):
            print(matriz[i][j], end="  ")
        print()
    print()

    for i in range(l):
        for j in range(c):
            matriz_TR[i][j] = matriz[j][i]
    
    print('MATRIZ TRANSPOSTA↓')
    for i in range(l):
        for j in range(c):
            print(f'{matriz_TR[i][j]}', end="  ")
        print()
    print()

    for i in range(l):
        for j in range(c):
            matriz_OP[i][j] = (matriz[i][j])*-1
    
    print('MATRIZ OPOSTA↓')
    for i in range(l):
        for j in range(c):
            print(matriz_OP[i][j], end="  ")
        print()
    print()

    for i in range(l):
        for j in range(c):
            if(matriz_TR[i][j] == matriz_OP[i][j]):
                cont += 1

    if(cont == l*c):
        print('!!!A matriz é ANTI-SIMÉTRICA!!!')
    else:
        print('A matriz não é ANTI-SIMÉTRICA!')

else:
    print('A matriz naõ é quadrada!')