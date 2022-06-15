a = str(input('Digite a maneira que você quer informar sua idade ANOS, MESES ou DIAS: '))

if(a in 'anos' or a in 'ANOS' or a in 'Anos'):
  anos = float(input('Digite a sua idade: '))
  print('A sua idade é de: ', anos*365, ' dias.')

if(a in 'meses' or a in 'MESES' or a in 'Meses'):
  meses = float(input('Digite a sua idade: '))
  print('A sua idade é de: ', meses*30, ' dias.')

#if(a in 'dias' or a in 'DIAS' or a in 'Dias'):
 # dias = float(input('A sua idade em dias é: '))
  # print('A sua idade é de: ', dias, ' dias.')

else:
  print('Houve um erro de digitação!')  