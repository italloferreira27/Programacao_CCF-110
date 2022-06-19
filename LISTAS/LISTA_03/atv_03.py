#maior = 0.0
#menor = 0.0
for i in range(0, 5):#1000
  num = float(input())
  if(i == 0):
    maior = num
    menor = maior
  elif(num < menor):
    menor = num
    #print('A1 = ', num)
  elif(num > maior):
    maior = num
    #print('B = ', maior)
print('O maior número é:', maior)
print('O menor número é:', menor)