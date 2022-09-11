l, a, p, r = map(float, input().split(" "))
aa = (a**2 + l**2 + p**2)**0.5
if(aa <= (2*r)):
  print('S')
else: 
  print('N')