while(True):
    n = int(input())
    if(n == 0):
        break

    matriz = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            matriz[i][j] = 2**(i+j)
    
    tam = len(str(matriz[n-1][n-1]))
    for i in range(n):
        for j in range(n):
            matriz[i][j] = str(matriz[i][j])
            while len(matriz[i][j]) < tam:
                matriz[i][j] = ' ' + matriz[i][j]
        resultado = ' '.join(matriz[i])
        print(resultado)
    print()