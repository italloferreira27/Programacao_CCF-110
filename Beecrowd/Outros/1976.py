# 1976
cont = 0
while True:
    n = int(input())
    if(n > 0):
        matriz = [[0 for j in range(1)] for i in range(n)]

        for i in range(n):
            matriz[i].append(list(map(int, input().split(" "))))
        print(matriz)

        #for i in range(n):
            
    else:
        break