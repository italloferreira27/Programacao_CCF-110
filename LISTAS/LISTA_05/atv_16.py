#EX. 16
nome = 'p'
id = 0
i = 1
while(nome != '@'):
  nome = str(input('Digite seu nome: '))
  if(nome != '@'):
    sexo = str(input('Digite seu sexo(f | FEMININO ou m | MASCULINO): '))
    idade = int(input('Digite sua idade: '))
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    if(sexo == 'm'):
      if(altura > maior):
        maior = altura
        nomea = nome
    if(sexo == 'f'):
      if(peso > mp):
        mp = peso
        nomep = nome
    id = id + idade
    i = i + 1
print(f"O maior atleta é {nomea} com {maior} de altura.")
print(f"A atleta {nomep} é a mais pesada com {mp} kg.")
print('A média das idades dos atletas é de: ', id/i)