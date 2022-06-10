print('\n!!!ATENÇÃ0!!! (Digite um numero negativo no numero da conta para parar o programa)')
num = 0
numerodaconta = []
saldo = []
contaclientes = 0
saldonegativo = 0
saldoagencia = 0
i = 0

while (num >= 0):
    num = int(input('Número da conta: '))
    if(num >= 0):
        numerodaconta.append(num)
        saldo.append(float(input('Saldo: ')))
        if(saldo[i] < 0):
            saldonegativo += 1
        saldoagencia += saldo[i]
        contaclientes += 1
        i += 1
percentualnegativo = (saldonegativo/contaclientes)*100
print('RELAÇÃO(|N° CONTA|   |SALDO|):')
for i in range(contaclientes):
    print(f"|{numerodaconta[i]}|   |R$ {saldo[i]:.2f}|")
print('\nTotal de cliente na agência: ', contaclientes)
print(f"Saldo total da agência: R$ {saldoagencia:.2f}")
print(f"Percentual das pessoas com o saldo negaativo: {percentualnegativo:.2f}%")        