n = int(input('Digite o tamanho do vetor: '))
vetor = [0 for i in range(n)]
soma = 0 
cont = 0
media = 0
mprox = 0

print('Preencha o vetor: ')
for i in range(n):
    vetor[i] = float(input())
    soma += vetor[i]
    cont += 1

media = soma/cont
mprox = media
for i in range(n):
    if(((vetor[i] - media) < mprox) and ((vetor[i] - media) >= 0)):
        mprox = vetor[i] - media
        valor = vetor[i]

print('Vetor = ', vetor)
print(f'(Média = {media:.1f})')
print('Valor mais próximo da média = ', valor)