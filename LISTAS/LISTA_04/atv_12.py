nota1 = float(input('Digigite sua 1ª nota: '))
nota2 = float(input('Digigite sua 2ª nota: '))
media = (nota1 + nota2)/2
if(media >= (70)):
  print('APROVADO!')
elif(media <= 30):
  print('REPROVADO!')
else:
  print('EXAME!')