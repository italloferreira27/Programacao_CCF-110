def infinity():
  i = 0
  while True:
    i = i + 1
    yield i
print('VOTAÇÃO: "digite 0 para parar"')
print('Digite o seu voto, sendo os candidatos de 1 ao 4 | 5 voto nulo | 6 = voto em branco:')
a = 0
tc1 = 0
tc2 = 0
tc3 = 0
tc4 = 0
n = 0
b = 0
for i in infinity():
  a = int(input('DIGITE SEU VOTO:'))
  if(a > 0):
    if(a == 1):
      tc1 = tc1 + 1
    elif(a == 2):
      tc2 = tc2 + 1
    elif(a == 3):
      tc3 += 1
    elif(a == 4):
      tc4 += 1
    elif(a == 5):
      n += 1
    elif(a == 6):
      b += 1
  else:
    print('Votos no candidato 1: ', tc1)
    print('Votos no candidato 2: ', tc2)
    print('Votos no candidato 3: ', tc3)
    print('Votos no candidato 4: ', tc4)
    print('Votos nulos: ', n)
    print('Votos em branco: ', b)
    print('Percentual dos votos nulos e brancos: %.2f' %((n+b)/(tc1+tc2+tc3+tc4+n+b)*100), '%')
    break