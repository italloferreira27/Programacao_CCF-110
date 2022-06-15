vetor1 = [0 for i in range(10)]
vetor2 = [0 for i in range(10)]

for i in range(10):
    vetor1[i] = int(input())

for i in range(10):
    vetor2[9-i] = vetor1[i]
print(vetor2)
