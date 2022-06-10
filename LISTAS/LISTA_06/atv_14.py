id = []
valor = []
valortotal = 0
numid = 0
i = 0
contador = 0
while(numid >= 0):
    numid = int(input('ID: '))
    if(numid >= 0):
        id.append(numid)
        valor.append(float(input('R$ ')))
        valortotal += valor[i]
        contador += 1
        i += 1
print('\nREGISTRO (|ID|  |R$0.00|): ')
for i in range(contador):
    print(f"|{id[i]}|  |R${valor[i]:.2f}|")
print(f'\nTotal de clientes {contador} e valor do caixa: R$ {valortotal:.2f}\n')