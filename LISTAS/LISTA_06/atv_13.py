#TESTANDO
vetor = [0 for i in range(5)]#15
crescente = []
d = 5 #15
t = 0
for i in range(5):#15
    vetor[i] = int(input())
#vetor.sort(reverse=True) #DECRESCENTE
#vetor.sort() #CRESCENTE
for i in range(5):#15
    for j in range(5):#15
        if(vetor[i] < vetor[j]):
            crescente.append(vetor[i])
            vetor.remove(vetor[i])
            t += 1
    if(t == 0):
        vetor.append(vetor[i])
        vetor.remove(vetor[i])
        t += 1
        d += 1
        t = 0 

print(crescente)
