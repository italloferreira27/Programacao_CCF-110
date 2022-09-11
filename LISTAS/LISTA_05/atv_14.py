#EX. 14
a1 = int(input('Digte o primeiro termo:'))
a2 = int(input('Digite o segundo termo:'))
n = int(input('Digite a quantidade de termos:'))
for i in range(1, n+1):
  if(i%2==0):
    #Par
    total = a1 - a2
  else:
    #Ímpar
    total = a1 + a2
  print(f"({i}) {a1} {a2} Total: {total}")
  a2 = a1
  a1 = total