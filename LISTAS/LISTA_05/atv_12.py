#EX. 12
x = float(input('Digite o valor em graus:'))
rad = ((x*3.14159265359)/180)
q = 3
c = 1
senx = 0
print(rad)
for i in range(15):
  qq = q
  for j in range(1, q, 1):
    qq = (qq * (q-j))
  senx = (rad - (((rad**q)/qq)*c))
  #print(q," ",qq)
  qq = 0
  c *= -1
  q += 2
  #print(senx)
print(f"Seno de {x}° é: {senx}")