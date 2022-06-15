a = int(input('Digite sua idade: '))
if(a >= 16 and  a <= 18 or a > 65):
  print('Eleitor facultativo!')
if(a < 16):
  print('Não é eleitor!')
elif(a >= 18 and a <= 65):
  print('Eleitor obrigatório!')