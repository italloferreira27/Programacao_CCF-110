n = int(input())
x = [0 for i in range(n)]
menor = 0
p = 0
for i in range(n):
    x = list(map(int, input().split(" ")))

for i in range(n):
    if(i == 0):
        menor = x[i]
    if(x[i] < menor):
        menor =  x[i]
        p = i

print(f'Menor valor: {menor}')
print(f'Posicao: {p}')