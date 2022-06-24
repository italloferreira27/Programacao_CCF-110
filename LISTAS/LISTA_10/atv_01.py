import random
vetor1 = [0 for i in range(10)]

for i in range(10):
    #vetor1[i] = random.randrange(0, 10)
    vetor1[i] = int(input())

maior = vetor1[0]
for i in range(10):
    #if(i == 0):
    if(vetor1[i] > maior):
        maior = vetor1[i]

#for i in range(10):
 #   for j in range(i+1, 10):
  #      if(vetor1[i] > )

vetor2 = [0 for i in range(maior)]
for i in range(maior):
    vetor2[i] = i+1
    cont = 0
    for j in range(10):
        if(vetor2[i] == vetor1[j]):
            cont += 1
            #vetor2[i] += 1
    vetor2[i] = cont
print(vetor1, '\n')
print(vetor2)