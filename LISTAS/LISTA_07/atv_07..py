par = []
impar = []
somapar = 0
contapar = 0
contaimpar = 0
somaimpar = 0

for i in range(50):
    n = int(input())
    if(n % 2 == 0):
        par.append(n)
        somapar += par[contapar]
        contapar += 1
    else:
        impar.append(n)
        somaimpar += impar[contaimpar]
        contaimpar += 1

print(f'Media dos números pares: {somapar/contapar:.1f}')
print(f'Media dos números ímpares: {somaimpar/contaimpar:.1f}')
print(f'\nNumeros PARES maiores que a media:')
for i in range(contapar):
    if(par[i] > (somapar/contapar)):
        print(f'|{par[i]}|', end="  ")
print(f'\nNumeros IMPARES menores que a media:')
for i in range(contapar):
    if(impar[i] < (somaimpar/contaimpar)):
        print(f'|{impar[i]}|', end="  ")