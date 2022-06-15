vetor = [0 for i in range(10)]
soma = 0
for i in range(10):
    vetor[i] = int(input())
    soma += vetor[i]
print('A média dos valores desse vetor é: ', soma/10)