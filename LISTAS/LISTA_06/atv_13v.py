vetor = [0 for i in range(5)]#15
crescente = 0

for i in range(5):#15
    vetor[i] = int(input())

for i in range(5):#15
    for j in range(i+1, 5):#15
        if(vetor[i] > vetor[j]):
            crescente = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = crescente
            #.........=..........
            #crescente = vetor[j]
            #vetor[j] = vetor[i]
            #vetor[i] = crescente
print(vetor)