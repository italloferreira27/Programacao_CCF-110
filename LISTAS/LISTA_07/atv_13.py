vetorA = []
vetorB = []
guarda = 0

print('Preencha o vetor A')
for i in range(5):#30
    vetorA.append(int(input()))

print('Preencha o vetor B')
for i in range(5):#30
    vetorB.append(int(input()))

x = int(input('Digite a variavel x: '))

for i in range(5):#30
    if(vetorA[i] == x):
        guarda = i 

if(guarda != 0): 
    print(f'O {vetorB[guarda]} é o N° do vetor B que está na mesma posição do N° {vetorA[guarda]} do vetor A que é = {x}')