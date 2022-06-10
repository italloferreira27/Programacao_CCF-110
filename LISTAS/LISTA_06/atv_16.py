from stringprep import in_table_c3


tamvetor = int(input('Digite o tamanho do vetor: '))
vetor_1 = []
vetor_2 = []
vetor_3 = []

print('PREENCHA O VETOR 1:')
for i in range(tamvetor):
    vetor_1.append(int(input()))

print('PREENCHA O VETOR 2:')
for i in range(tamvetor):
    vetor_2.append(int(input()))

for i in range(tamvetor):
    vetor_3.append(vetor_1[i])
    vetor_3.append(vetor_2[i])

print(f"\nVetor 1: {vetor_1}\nVetor 2: {vetor_2}\nVetor 3: {vetor_3}")