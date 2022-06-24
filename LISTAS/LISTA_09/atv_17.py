#https://www.youtube.com/watch?v=V6ul0t_M8hk
#https://www.youtube.com/watch?v=WK1SmFAPLOw&t=790s
c = int(input('C: '))
d = int(input('D: '))
e = int(input('E: '))
f = int(input('F: '))
A = [[0 for j in range(d)] for i in range(c)]
B = [[0 for j in range(f)] for i in range(e)]
G = [[0 for j in range(f)] for i in range(c)]
cont = 0

if(d == e):
    print('Preencha a matriz A[CxD]')
    for i in range(c):
        for j in range(d):
            A[i][j] = int(input())
    print()

    print('Preencha a matriz B[ExF]')
    for i in range(e):
        for j in range(f):
            B[i][j] = int(input())
#.....ESCREVENDO AS MATRIZES A E B .....
    print('\nMatriz A ↓')
    for i in range(c):
        for j in range(d):
            print(A[i][j], end="  ")
        print()
    print()

    print('Matriz B ↓')
    for i in range(e):
        for j in range(f):
            print(B[i][j], end="  ")
        print()
    print()
#.......................................
    #Multiplicando as raízes
    for i in range(c):
        for j in range(f):
            for k in range(d):
                G[i][j] += A[i][k] * B[k][j]
            
    print('\nMatriz G ↓')
    for i in range(c):
        for j in range(f):
            print(G[i][j], end="  ")
        print()
else:
    print('Não é possível multiplicar essas matrizes!')