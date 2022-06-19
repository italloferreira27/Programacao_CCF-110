a = int(input('Digite o número para fatorar:'))
if(a != 0):
  for i in range(a, 0, -1):
    b = a
    b1 = b + (b * i)  
  print(a, 'fatorial é:', b1)  
else:
  print(a, 'fatorial é: 1')