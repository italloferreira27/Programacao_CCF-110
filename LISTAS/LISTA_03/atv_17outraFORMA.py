#https://docs.python.org/pt-br/3/tutorial/inputoutput.html
n = 1 #numerador que vai de 2 em 2
d = 1 #denominador que vai de 1 em 1
soma = 0
for i in range(1, 51):
  soma += n/d
  n += 2
  d += 1
print(soma)