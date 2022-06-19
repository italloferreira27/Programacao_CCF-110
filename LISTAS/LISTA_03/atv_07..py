a = 0
b = 0
for i in range(0, 4):#200):
  num = float(input())
  if(num%2 == 0):
      a = a + 1
  else: 
      b = b + 1
print('Números pares:', a)
print('Números ímpares:', b)