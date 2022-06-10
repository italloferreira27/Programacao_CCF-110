totalcaixas = int(input('Digite o N° total de caixas: '))
valormonetario = int(input('Valor monetario da carga: '))
kgcaixa = []
precocaixa = []
contapeso = 0
contavalor = 0
for i in range(totalcaixas):
    kgcaixa.append(float(input('Digite o peso em kg da caixa: ')))
    precocaixa.append(float(input('Digite o valor da caixa: ')))
    contavalor += precocaixa[i]
    contapeso += kgcaixa[i]
print('Peso total descarregado: ', contapeso, 'KG')
if(valormonetario == contavalor):
    print('Valor válido! R$ ', contavalor)
else:
    print('\nValor inválido!\nValor monetário: R$', valormonetario,'\nValor descarregado: R$', contavalor)
