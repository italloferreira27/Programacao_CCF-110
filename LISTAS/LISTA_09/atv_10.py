cont = 1
matriz = [[0 for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        matriz[i][j] = cont
        cont += 1

#MINHA MATRIZ INICIAL
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]}', end="  ")
    print()    
print()

#MATRIZ GIRA 180°
for i in range(2, -1, -1):
    for j in range(2, -1, -1):
        print(f'{matriz[i][j]}', end="  ")
    print()