import random
n = int(input('Digite um numero: '))
vetor = []
cont = 0

for i in range(n):
    #vetor[i] = int(input())
    vetor.append(random.randrange(0, 100))

print('DESORGANIZADO: ',vetor)
for i in range(n):
    for j in range(i+1, n):
        if(vetor[i] > vetor[j]):
            cont = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = cont
print('Vetor na ordem crescente: ',vetor)

cont = 0
for i in range(n):
    for j in range(i+1, n):
        if(vetor[i] < vetor[j]):
            cont = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = cont
print('Vetor na ordem decrescente: ',vetor)