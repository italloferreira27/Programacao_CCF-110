sal = float(input()) 

if(sal > 0 and sal <= 400.00):
  nsal = sal * 1.15
  rea = nsal - sal
  print('Novo salario: %.2f' %nsal)
  print('Reajuste ganho: %.2f' %rea)
  print('Em percentual: 15 %')

if(sal >= 400.01 and sal <= 800.00):
  nsal = sal * 1.12
  rea = nsal - sal
  print('Novo salario: %.2f' %nsal)
  print('Reajuste ganho: %.2f' %rea)
  print('Em percentual: 12 %')

if(sal >= 800.01 and sal <= 1200.00):
  nsal = sal * 1.1
  rea = nsal - sal
  print('Novo salario: %.2f' %nsal)
  print('Reajuste ganho: %.2f' %rea)
  print('Em percentual: 10 %')
  
if(sal >= 1200.01 and sal <= 2000.00):
  nsal = sal * 1.07
  rea = nsal - sal
  print('Novo salario: %.2f' %nsal)
  print('Reajuste ganho: %.2f' %rea)
  print('Em percentual: 7 %')
  
if(sal > 2000.00):
  nsal = sal * 1.04
  rea = nsal - sal
  print('Novo salario: %.2f' %nsal)
  print('Reajuste ganho: %.2f' %rea)
  print('Em percentual: 4 %')

  print(kkkkkk)
  