#EX. 11
subtracao = 0
a = int(input())
b = int(input())
quoc = 0
while (a >= b):
  a = a - b
  quoc += 1
print('Quociente:',quoc)
print('Resto:', a)