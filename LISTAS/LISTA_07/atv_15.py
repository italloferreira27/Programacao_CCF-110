n = int(input('Entre com a quantidade de números: '))
vetor = []
repeat = []
vtcont = []
troca = 0
cont = 0
tamfor = 0

for i in range(n):
    vetor.append(int(input()))

for i in range(n):
    for j in range(i+1, n):
        if(vetor[i] > vetor[j]):
            troca = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = troca
print('Vetor ordenado: ', vetor, '\n')

for i in range(n):
    for j in range(i+1, n):
        if(vetor[i] == vetor[j] and i == 0):
            cont += 1
        elif(vetor[i] != vetor[i-1] and vetor[i] == vetor[j]):
            cont += 1
    
    if(cont != 0):
        vtcont.append(cont)
        repeat.append(vetor[i])
        tamfor += 1

    cont = 0
for i in range(tamfor):
    if(vtcont[i] > 1):
        print(f'O número {repeat[i]} apareceu mais {vtcont[i]} vezes.')
    else:
        print(f'O número {repeat[i]} apareceu mais {vtcont[i]} vez.')