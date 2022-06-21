print('__' *10)
print('1 | REGIÃO NORTE')
print('__' *10)
print('2 | REGIÃO NORDESTE')
print('__' *10)
print('3 | REGIÃO CENTRO-OESTE')
print('__' *10)
print('4 | REGIÃO SUL\n')
destino = int(input('Informe o seu destino:'))
ida = int(input('Sua via gem inclui ida e volta? 1 para sim e 2 para não:'))
if(destino == 1 and ida == 1):
  print('Região norte ida e volta R$900,00')
elif(destino == 1 and ida == 2):
  print('Região norte ida R$500,00')
elif(destino == 2 and ida == 1):
  print('Região nordeste ida e volta R$650,00')
elif(destino == 2 and ida == 2):
  print('Região nordete ida R$350,00')
elif(destino == 3 and ida == 1):
  print('Região Centro-Oeste ida e volta R$600,00')
elif(destino == 3 and ida == 2):
  print('Região Centro-Oeste ida R$350,00')
elif(destino == 4 and ida == 1):
  print('Região Sul ida e volta R$550,00')
elif(destino == 4 and ida == 2):
  print('Região Sul ida R$300,00')