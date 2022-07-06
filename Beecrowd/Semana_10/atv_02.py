n = int(input())
x = []
menor = 0
p = 0
#for i in range(n):
x = [int(x) for x in input().split()]

for i in range(n):
    if(i == 0):
        menor = x[i]
    if(x[i] < menor):
        menor =  x[i]
        p = i

print(f'Menor valor: {menor}')
print(f'Posicao: {p}')