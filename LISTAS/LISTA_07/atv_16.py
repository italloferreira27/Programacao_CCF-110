import random
vetorB = []
somatorio = 0

for i in range(100):
    #vetorB.append(int(input()))
    vetorB.append(random.randrange(1, 100))

for i in range(50):
    somatorio += ((vetorB[i] - vetorB[99-i])**3)

print('Somatório:', somatorio)