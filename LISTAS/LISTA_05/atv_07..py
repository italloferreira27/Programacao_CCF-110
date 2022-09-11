#EX. 07
num = 0
i = 0
soma = 0
while (num != -1):
  num = int(input())
  if(num %3== 0):
    i += 1
    soma += num
print('A média dos multiplos de 3 é:', soma/i)