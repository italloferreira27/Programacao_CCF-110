import random
n = int(input('Numeros de funcionarios:'))
matriz = [[0 for j in range(3)] for i in range(n)]
soma = 0
somap = 10
somam = 15
somapm = 30
vetorsal = []

for i in range(n):
    for j in range(3):
        #matriz[i][j] = int(input())
        matriz[i][j] = random.randrange(0, 6)
        if(matriz[i][0]):
            somap *= (matriz[i][j])
            soma += somap
        if(matriz[i][1]):
            somam *= (matriz[i][j])
            soma += somam
        if(matriz[i][2]):
            somapm *= (matriz[i][j])
            soma += somapm
    vetorsal.append(soma*0.5)
    soma = 0
    somap = 10
    somam = 15
    somapm = 30
            
#Copia nao↓
for i in range(n):
    for j in range(3):
        print(f'{matriz[i][j]}', end="  ")
    print()
print()
#.........

for i in range(n):
    print(f'Funcionario {i} recebeu R${vetorsal[i]}')