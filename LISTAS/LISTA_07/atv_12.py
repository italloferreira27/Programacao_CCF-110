import random
vetor = []
frequencia = 0
frequenciaabsl = [0 for i in range(11)]
freqrel = 0
for i in range(80):
    #vetor.append(int(input()))
    vetor.append(random.randrange(0, 11))

print('NOTAS:', vetor)

for i in range(11):
    for j in range(80):
        if(i == vetor[j]):
            frequencia += 1
            frequenciaabsl[i] = frequencia
    frequencia = 0

print('         |FREQ. absoluta|  |FREQ. relativa|')
for i in range(11):
    freqrel = (frequenciaabsl[i] / 80)*100
    print(f'NOTA: {i}  |{frequenciaabsl[i]:^14}|  |{freqrel:^13.2f}%|')