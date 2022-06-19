#https://www.horadecodar.com.br/2020/04/27/python-para-que-serve-o-yield-quando-utilizar/
#https://stackoverflow.com/questions/9884213/looping-from-1-to-infinity-in-python9

def infinity():
    i=0
    while True:
        i+=1
        yield i
b = 0
num1 = 0
for i in infinity():
  num = int(input('Digite os n°:'))
  if(num != -1):
     num1 += num
     b = b + 1
  else:
     print('A media dos', b, 'numeros é de:', num1/b)
     break