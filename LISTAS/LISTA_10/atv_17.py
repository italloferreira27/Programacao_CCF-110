data = input('Digite sua data de nascimento (dd/mm/aaaa)').split("/")
meses = ['','janeiro','feverreiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

if(data[1][0] == '0'):
    print(f'Você nasceu mo dia {data[0]} de {meses[int(data[1][1])]} de {data[2]}')
else:
    print(f'Você nasceu mo dia {data[0]} de {meses[int(data[1])]} de {data[2]}')