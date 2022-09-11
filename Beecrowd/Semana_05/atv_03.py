dis = 0
cont = 0
while True:
  try:
    nome = str(input())
    distancia = int(input())
    dis += distancia
    cont += 1
  except:
    break
media = dis/cont
print('%.1f' %media)