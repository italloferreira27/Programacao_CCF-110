matriz = [[0 for j in range(2)] for i in range(2)]
determinante = 0
dp = 1
ds = 1
cont = 1
for i in range(2):
    for j in range(2):
        matriz[i][j] = int(input())
        #matriz[i][j] = cont
        cont += 1

for i in range(2):
    for j in range(2):
        print(f'{matriz[i][j]}', end=" ")
    print()

for i in range(2):
    for j in range(i, i+1):
        dp *= matriz[i][j]
    for j in range(1-i, 2-i):
        ds *= matriz[i][j]

print(f'Prod_dp: {dp}   Prod_ds: {ds}')
determinante = dp - ds

print(determinante)