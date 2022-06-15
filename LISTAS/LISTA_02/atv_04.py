a = float(input('Digite a sua idade em dias: '))
b = str(input('Escolha como você quer ver a sua idade? DIAS, MESES, ANOS ou TODAS AS OPCOES: '))
aa = 0
if(b in 'dias' or b in 'DIAS' or b in 'Dias'):
  print('A sua idade em dias é: ', a)

elif(b in 'meses' or b in 'MESES' or b in 'Meses'): 
  print('A sua idade em meses é: ', a/30)

elif(b in 'anos' or b in 'ANOS' or b in 'Anos'):
  aa = a/365
  print('A sua idade em anos é: %.2f' %aa)

elif(b in 'todas as opcoes' or b in 'TODAS AS OPCOES' or b in 'Todas as opcoes'):
  print('A sua idade em dias é: ', a)
  print('A sua idade em meses é: ', a/30)
  print('A sua idade em anos é: %.2f' %aa)

else:
  print('HOUVE UM ERRO DE DIGITAÇÃO!')