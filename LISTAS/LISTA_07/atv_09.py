import random
temperatura = [0 for i in range(121)]
soma = 0

for i in range(121):
    #temperatura[i] = int(input())
    temperatura[i] = random.randrange(15, 41)
    soma += temperatura[i]

    if(i == 0):
        menor = temperatura[i]
        maior = temperatura[i]
    if(temperatura[i] > maior):
        maior = temperatura[i]
    if(temperatura[i] < menor):
        menor = temperatura[i]
print('A maior temperatura foi de: ', maior)
print('A menor temperatura foi de: ', menor)
print(f'A media das temperaturas:  {soma/121:.2f}')
print('Dias em que a temperatura foi menor do que a media:')
for i in range(121):
    if(temperatura[i] < (soma/121)):
        print(f'|{temperatura[i]}|', end=" ")