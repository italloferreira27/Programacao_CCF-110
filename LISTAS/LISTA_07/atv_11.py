n = int(input())
vetor = []
troca = 0
newvetor = []
vtcont = []
valor = []
cont = 1
tamfor = 0

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
            cont += 1
            tamfor += 1
            valor.append(vetor[j])
            vetor[j] = 0
    if(cont > 1):
        vtcont.append(cont)
    cont = 1

for i in range(n):
    if(vetor[i] != 0):
        newvetor.append(vetor[i])

print('Novo vetor sem número repetido: ',newvetor)
for i in range(tamfor):
    print(f'O número {valor[i]} repetiu {vtcont[i]} vezes.')

print(vtcont)