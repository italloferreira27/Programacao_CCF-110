#https://www.ime.usp.br/~macmulti/exercicios/inteiros/2Python.html
d = 1 #denominador que vai de 38 em 1
n = 0 #numerador que vai de 1 ao 37
c = 1 #contador
for i in range(37, 0, -1):
  n += (i * (i+1)) / c
  c += 1   
print(n) 