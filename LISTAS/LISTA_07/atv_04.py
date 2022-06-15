vetor = []
for i in range(5):#30
    vetor.append(int(input()))
    if(vetor[i] % 2 == 0):
        vetor[i] = 0
print(f'VETOR ATUALIZADO↓')
print(vetor)