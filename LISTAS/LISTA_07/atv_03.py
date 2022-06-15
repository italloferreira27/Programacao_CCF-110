vetor = [0 for i in range(15)]
posimaior = 0
posimenor = 0
for i in range(15):
    vetor[i] = int(input())
    if(i == 0):
        maior = vetor[0]
        menor = vetor[0]
    if(vetor[i] > maior):
        maior = vetor[i]
        posimaior = i
    if(vetor[i] < menor):
        menor = vetor[i]
        posimenor = i

print('O numero maior é: ', maior, 'e está na posição ', posimaior)
print('O numero menor é: ', menor, 'e está na posição ', posimenor)