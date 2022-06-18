n = int(input())
vetor = []
troca = 0
newvetor = []
print('Preencha o vetor: ')
for i in range(n):
    vetor.append(int(input()))

print('Vetor Digitado: ', vetor)
for i in range(n):
    for j in range(i+1, n):
        if(vetor[i] > vetor[j]):
            troca = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = troca

print(f"Vetor em ordem crescente: {vetor}")

for i in range(n):
    for j in range(i+1, n):
        if(vetor[i] == vetor[j]):
            #vetor.remove(vetor[j])
            vetor[j] = 0

for i in range(n):
    if(vetor[i] != 0):
        newvetor.append(vetor[i])

print('Novo vetor sem número repetido: ',newvetor)