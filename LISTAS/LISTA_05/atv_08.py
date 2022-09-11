#EX. 08
num = 0
i = 0
ma = 0
me = 0
while(num != -1):
  i += 1
  num = int(input(''))
  if(num != -1):
    if(i == 1):
      menor = num
      maior = num
    if(num < menor):
      me = num
    if(num > maior):
      ma = num
print(f"O número maior registrado foi {ma} e o menor foi {me}")
