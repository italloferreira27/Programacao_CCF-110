a = int(input('Digite sua idade:'))
b = float(input('Digite seu peso:'))
if(a >= 12 and b >= 60):
  print('Vc deve tomar 1000mg ou 40 gotas.')
elif(a >= 12 and b < 60):
  print('Vc deve tomar 875mg ou 35 gotas.')  
elif(a < 12):
  p1 = tuple(range(5, 9))
  p2 = tuple(range(9, 16))
  p3 = tuple(range(16, 24))
  p4 = tuple(range(24, 30))
  if(b in p1):
    print('Vc deve tomar 125mg ou 5 gotas.')
  if(b in p2):
    print('Vc deve tomar 250mg ou 10 gotas.')
  if(b in p3):
    print('Vc deve tomar 275mg ou 11 gotas.')
  if(b in p4):
    print('Vc deve tomar 500mg ou 20 gotas.')
  if(b > 30):
    print('Vc deve tomar 750mg ou 30 gotas.')  
if(b < 5):
  print('Peso inválido!')    