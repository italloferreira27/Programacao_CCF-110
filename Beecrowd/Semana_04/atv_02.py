sal = float(input())
if(sal >=0.00 and sal <=2000.00):
  print('Isento')
elif(sal >= 2000.01 and sal <= 3000.00):
  a = sal - 2000
  aa = a * 0.08
  print('R$ %.2f' %aa)
elif(sal >= 3000.01 and sal <= 4500.00):
  a = sal - 3000
  aa = a * 0.18
  aa = aa + 80
  print('R$ %.2f' %aa)
elif(sal > 4500.00):
  a = sal - 4500
  aa = a * 0.28
  aa = aa + 350
  print('R$ %.2f' %aa)