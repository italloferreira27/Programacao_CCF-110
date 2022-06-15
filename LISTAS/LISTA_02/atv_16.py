a = int(input('Digite o mês do ano:'))
t1 = [1,2,3]
t2 = [4,5,6]
t3 = [7,8,9]
t4 = [10,11,12]
if(a >= 1 and a <= 12):
  if (a in t1):
    print('1º trimestre')
  if(a in t2):
    print('2º trimestre')
  if(a in t3):
    print('3º trimestre')
  if(a in t4):
    print('4º trimestre')
else:
  print('Mês inválido')