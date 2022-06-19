import random
corredor = []
troca = 0
compara = []
for i in range(10):
    #corredor.append(int(input('Digite seu tempo')))
    corredor.append(round(random.uniform(0, 10), 2))
    compara.append(corredor[i])

print(corredor)

for i in range(10):
    for j in range(i+1, 10):
        if(corredor[i] > corredor[j]):
            troca = corredor[i]
            corredor[i] = corredor[j]
            corredor[j] = troca

print('|Posição|   |Tempo|   |N° de inscrição|')
for i in range(10):
    print(f'|{i+1:^7}|   |{corredor[i]:^5}|   ', end="")
    for j in range(10):
        if(corredor[i] == compara[j]):
            print(f'|{j:^15}|')