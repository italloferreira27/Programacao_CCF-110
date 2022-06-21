s = 0
n = int(input('Digite o valor para n: '))
for i in range(0, n):
  s += (1/(2+i)**2+i)
print(1+s)