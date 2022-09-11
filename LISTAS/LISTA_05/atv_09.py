#EX. 09 
#raizes = 0
i = 2
while (i < 12):
  num = float(input())
  if(num >= 0):
    print(f"Raiz de {num} = {num**0.5}")
    i += 1
  else:
    print('Números inválidos! Digite outro positivo:')
    i -= 1 
'''
#EX. 09 Tentei com VETOR ERRO
#raizes = list(range(10))
raizes = []
for i in range(1, 3):
  num = float(input())
  if(num >= 0):
    raizes[i] = num**0.5
  else:
    print('Números inválidos! Digite outro positivo:')
    i -= 1 
print(f"Raizes dos números digitados: {raizes}")
'''