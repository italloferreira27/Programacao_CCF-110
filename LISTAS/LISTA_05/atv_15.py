#EX. 15 
print('A | ÓTIMO\nB | BOM\nC | REGULAR\nD | RUIM\nE | PÉSSIMO\n')
a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(1, 6):#100
  op = str(input('Digite sua opinião para o filme:'))
  id = int(input('Digite sua idade:'))
  if(i == 1):
    maiora = id
    maiord = id
  if(op == 'a'):
    a += 1
    if(id > maiora):
      maiora = id
  if(op == 'b'):
    b += 1
  if(op == 'c'):
    c += 1
  if(op == 'd'):
    d += 1
    if(id > maiord):
      maiord = id
  if(op == 'e'):
    e +=1
print('A quantidade de avaliações ótimas:', a)
print('A diferença percentual entre respostas bom e regular', ((b/100)-(c/100))*100, '%')
print(f"Porc. que responderam péssimo: {e/100}% e nº de pessoas = {e}.")
print('A diferença entre dos maiores de idade A e D são:', maiora - maiord)