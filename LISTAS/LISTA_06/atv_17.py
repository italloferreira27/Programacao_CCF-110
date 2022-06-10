quantcompra = int(input('Digite quantas compras foram feitas: '))
valormonetario = []
nomeproduto = []
for i in range(quantcompra):
    nomeproduto.append(input('Nome do produto: '))
    valormonetario.append(float(input('Valor do produto em dolar: US$')))
print('*'*10,'RELAÇÃO:','*'*10)
for i in range(quantcompra):
    print(f"Produto {nomeproduto[i]}, valor em US$ {valormonetario[i]:.2f}, valor em R$ {valormonetario[i]*4.9:.2f}")