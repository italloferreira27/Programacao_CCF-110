import random
matriz = [[0 for j in range(10)] for i in range(10)]
newmatriz = [[0 for j in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        #matriz[i][j] = int(input())
        matriz[i][j] = random.randrange(1, 10)

#TESTANDO!!! NÃO PRECISA COPIAR
for i in range(10):
    for j in range(10):
        print(f'{matriz[i][j]}', end="  ")
    print()
print()
#...............................
#print(matriz)
#print()

for i in range(10):
    matriz[i][9-i] = 0
    
for i in range(10):
    for j in range(10):
        if(matriz[i][j] != 0):
            #newmatriz[i][j] = matriz[i][j]
            print(matriz[i][j], end="  ")
    print()

#print(newmatriz)
#for i in range(10):
    #for j in range(10):
     #   print(f'{newmatriz[i][j]}', end="  ")
    #print()
