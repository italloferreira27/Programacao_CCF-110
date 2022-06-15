import random
x = random.randrange(0, 10)
print('Seu numero sorteado foi:', x)
#a = int(input('Digite a bola sorteada:'))
b = float(input('Digite o valor em caixa: R$'))
if(x == 0):
  print('Seu prêmio: R$', b*0.05)
if(x == 1):
  print('Seu prêmio: R$', b*0.25)
if(x == 2):
  print('Seu prêmio: R$', b*0.1)
if(x == 3):
  print('Seu prêmio: R$', b*0.07)
if(x == 4):
  print('Seu prêmio: R$', b*0.08)
if(x == 5):
  print('Seu prêmio: R$', b*0.05)
if(x == 6):
  print('Seu prêmio: R$', b*0.15)
if(x == 7):
  print('Seu prêmio: R$', b*0.12)
if(x == 8):
  print('Seu prêmio: R$', b*0.03)
if(x == 9):
  print('Seu prêmio: R$', b*0.10)