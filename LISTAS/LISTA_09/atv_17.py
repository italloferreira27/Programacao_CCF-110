#https://www.youtube.com/watch?v=V6ul0t_M8hk
c = int(input('C: '))
d = int(input('D: '))
e = int(input('E: '))
f = int(input('F: '))
A = [[0 for j in range(d)] for i in range(c)]
B = [[0 for j in range(f)] for i in range(e)]
G = [[0 for j in range(f)] for i in range(c)]

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
    
    

else:
    print('Não é possível multiplicar essas matrizes!')