#EX. 06
c =0
for i in range(1, 16):
  x = float(input())
  if(x > 30):
    c += 1
print('Foram digitados', c, 'números maiores que 30')