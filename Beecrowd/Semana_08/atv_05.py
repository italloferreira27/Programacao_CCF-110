while True:

    try:

        n = int(input())
        matriz = [[0 for j in range(n)]for i in range(n)]

        for i in range(n):
            for j in range(n):
                if(j == (n-1)-i):
                    matriz[i][j] = 2
                elif(i == j):
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 3
        
        for i in range(n):
            for j in range(n):
                print(f'{matriz[i][j]}', end="")
            print()                

    except EOFError:
        break

