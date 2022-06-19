def infinity():
  i = 0
  while True:
    i += i
    yield i
a1 = 1
a2 = 0
for i in infinity():
  a = int(input('Digite os valores:'))
  if(a > 0):
    if(a%2 != 0):
      a1 = a1 * a 
    elif(a%2 == 0):
      a2 = a2 + a
  else:
      print('O produto dos números ímpares é: ', a1)
      print('A soma dos números pares é: ', a2)   
      break