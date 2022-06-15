a = float(input('Digite um núemro: '))
b = float(input('Digite outro número: '))
c = float(input('Digite outro número: '))
if(a > b and b > c and a > c):
  print('Os números digitados na ordem descrescente são: ',a,'|',b,'|',c)

elif(a > b and b < c and a > c):
  print('Os números digitados na ordem descrescente são: ',a,'|',c,'|',b)

elif(b > a and a > c and b > c):
  print('Os números digitados na ordem descrescente são: ',b,'|',a,'|',c)

elif(b > a and a < c and b > c):
  print('Os números digitados na ordem descrescente são: ',b,'|',c,'|',a)

elif(c > a and a > b and c > b):
  print('Os números digitados na ordem descrescente são: ',c,'|',a,'|',b)

elif(c > a and a < b and c > b):
  print('Os números digitados na ordem descrescente são: ',c,'|',b,'|',a)

else:
  print('HOUVE ALGUM ERRO!')