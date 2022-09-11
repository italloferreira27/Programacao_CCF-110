#EX. 02
salmed = float(input('Digite o seu sálario médio do último ano:'))
if(salmed <= 500):
  print('Nenhum crédito!')
elif(salmed >= 501 and salmed <= 1000):
  print(f"Seu salário é R${salmed} e seu crédito diponivél é: {salmed*0.3}")
elif(salmed >= 1001 and salmed < 3000):
  print(f"Seu salário é R${salmed} e seu crédito é: R${salmed*0.4}")
elif(salmed > 3001):
  print(f"Seu salário é de R${salmed} e seu crédito é de: R${salmed*0.5}")