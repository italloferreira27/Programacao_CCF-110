vetor = [0 for i in range(15)]
numprimo = 0
primo = []
posicao = []
cont = 0

for i in range(15):
    vetor[i] = int(input())
    for j in range(1, (vetor[i]+1)):
        if(vetor[i] % j == 0):
            numprimo += 1
    if((numprimo == 2) or (vetor[i] == 1)):
        primo.append(vetor[i])
        posicao.append(i)
        cont += 1
    numprimo = 0

print('|Nº|   |Posição|:')
for i in range(cont):
    print(f'|{primo[i]}|       |{posicao[i]}|')