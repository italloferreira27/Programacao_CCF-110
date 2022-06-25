tam1 = int(input('Digite o tamanho do vetor 1: '))
tam2 = int(input('Digite o tamanho do vetor 2: '))
tm = tam1+tam2
vetor1 = [0 for i in range(tam1)]
vetor2 = [0 for i in range(tam2)]
vetorINT = [0 for i in range(tm)]
cont = 1

print('Preencha o vetor 1:')
for i in range(tam1):
    vetor1[i] = int(input())
#vetor1 = list(map(int, input().split(" "))) #MUITO ROUBADO

print('Preencha o vetor 2: ')
for i in range(tam2):
    vetor2[i] = int(input())
#vetor2 = list(map(int, input().split(" "))) #MUITO ROUBADO

if(tam1 < tam2):
    for i in range(tam1):
        vetorINT[i*2] = vetor1[i]
        vetorINT[i*2+1] = vetor2[i]
        cont += 1

    for i in range(cont, tm):
        vetorINT[i] = vetor2[i-tam1]

else:
    for i in range(tam2):
        vetorINT[i*2] = vetor2[i]
        vetorINT[i*2+1] = vetor1[i]
        cont += 1

    for i in range(cont, tm):
        vetorINT[i] = vetor1[i-tam2]

print('Vetor inteirado: ', vetorINT)