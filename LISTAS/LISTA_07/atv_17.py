import random
mercadoria = [0 for i in range(0, 100)]
arrecadado = [0 for i in range(0, 100)]
preco = [0 for i in range(0, 100)]
nummerc = 0
total = 0
for i in range(0, 100):
    #mercadoria[i] = int(input('Digite a quantidade de mercadoria vendida: '))
    mercadoria[i] = random.randrange(1, 101)
    #preco = float(input('Digite o valor da mercadoria: R$'))
    preco[i] = (round(random.uniform(10, 1000), 2))
    arrecadado[i] = mercadoria[i] * preco[i]
    total += arrecadado[i]

print('\n|N° mercadoria|   |Mercadoria Vendida|   |Valor da mercadoria (R$)|   |Valor arrecadado (R$)|')
for i in range(0, 100):
    print(f'|{i+1:^13}|   |{mercadoria[i]:^18}|   |{preco[i]:^24.2f}|   |{arrecadado[i]:^21.2f}|')
print('\nValor total adquirido nesse mês: R$%.2f' %total)