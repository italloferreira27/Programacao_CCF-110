b1 = 0
b2 = 0
bf = 0
bm = 0
print('Digite o seu voto (1 = masculino, 2 = feminino) e sua resposta (1 = sim, 2 = não):')
for i in range(5):#2000
   a = int(input('Sexo: '))
   b = int(input('Voto: '))
   if(b == 1):
     b1 += 1
   elif(b == 2):
     b2 += 1
   elif(a == 2 and b == 1):
     bf += 1
   elif(a == 1 and a == 2):
     bm += 1
print('O n° de pessoas que responderam SIM:', b1)
print('O n° de pessoas que responderam NÃO:', b2)
print('A porcentagem de pessoas do sexo feminino que responderam SIM:', (bf/2000)*100)
print('A porcentagem de pessoas do sexo Masculino que responderam NÃO:', (bm/2000)*100)