vetor = [0 for i in range(20)]
for i in range(20):
    vetor[i] = int(input())
    if(i == 0):
        maior = vetor[i]
        menor = vetor[i]
    if(vetor[i] >= maior):
        maior = vetor[i]
    if(vetor[i] <= menor):
        maior = vetor[i]

print('O valor maior é: ', maior)
print('O valor menor é: ', menor)