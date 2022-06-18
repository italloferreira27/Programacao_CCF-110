n = int(input())
salario = []
soma = 0
mediana = 0
med = 0
for i in range(n):
    salario.append(int(input()))
    soma += salario[i]

if(n % 2 == 0):
    med = (n // 2)
    mediana = ((salario[med - 1] + salario[med])/2)

else:
    med = n // 2
    mediana = salario[med]

media = soma/n
print(f'A média dos sálarios é: {media:.2f}')
print(f'A mediana é: {mediana:.2f}')