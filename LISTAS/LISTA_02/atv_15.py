a = int(input('Digite o dia da semana:'))
if(a >= 1 and a <= 7):
  if(a == 1):
    print('DOMINGO!')
  if(a == 2):
    print('SEGUNDA!')
  if(a == 3):
    print('TERÇA!')
  if(a == 4):
    print('QUARTA!')
  if(a == 5):
    print('QUINTA!')
  if(a == 6):
    print('SEXTA!')
  if(a == 7):
    print('SÁBADO!')
else:
  print('Dia da semana inválido!')