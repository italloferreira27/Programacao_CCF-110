#http://ednilsonrossi.blogspot.com/2016/04/logica-serie-de-ricci.html
aux = 0
soma = 0
i = 0
num1, num2 = map(int, input().split(" "))
n = int(input('Digite N: '))
if(n > 3):
  while i < n:
    aux = num1 + num2
    print(aux, end=" ")
    soma = soma + aux
    num1 = num2
    num2 = aux
    i += 1
  print('\nSoma dos termos:', soma)