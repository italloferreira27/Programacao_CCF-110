n = int(input('Digite o valor de n: '))
vetor = [0 for i in range(n)]
troca = 0
valor = 0

print('Preencha o vetor: ')
for i in range(n):
    vetor[i] = int(input())

k = int(input('Digite o valor de k: '))
print('ANTES: ', vetor)
valor = vetor[k]

for i in range(n):
    for j in range(i+1, n):
        if(vetor[i] > vetor[j]):
            troca = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = troca
print('DEPOIS: ', vetor)
print('O k-ésimo termo do vetor antes de ordenar é: ', valor)
print('O k-ésimo termo do vetor depois de ordenar é: ', vetor[k])