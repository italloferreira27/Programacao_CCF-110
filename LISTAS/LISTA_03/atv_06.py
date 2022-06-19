x = int(input('Digite um número x:'))
z = int(input('Digite um número z:'))
if(x < z):
  for i in range(x, z+1, 1):
      print(i)
else:
  for i in range(z, x+1, 1):
      print(i)