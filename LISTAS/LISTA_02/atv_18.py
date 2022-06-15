a = float(input('Digite o peso na terra:'))
b = str(input('Digite o planeta, \nm(MERCURIO)\nv(VÊNUS)\nr(MARTE)\nj(JÚPITER)\ns(SATURNO)\nu(URANO)\n:'))
if(b in 'm'):
  print('Peso é de: %.2f' %(a*0.37))
if(b in 'v'):
  print('Peso é de: %.2f' %(a*0.88))
if(b in 'r'):
  print('Peso é de: %.2f' %(a*0.38))
if(b in 'j'):
  print('Peso é de: %.2f' %(a*2.64))
if(b in 's'):
  print('Peso é de: %.2f' %(a*1.15))
if(b in 'u'):
  print('Peso é de: %.2f' %(a*1.17))