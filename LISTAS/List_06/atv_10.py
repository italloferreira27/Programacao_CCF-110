nota = [0 for i in range(3)]#10
nome = []
nomemenor = 's'
nomemaior = 's'
notamaior = 0
nomemenor = 0
menor = 0
maior = 0
for i in range(3):#10
    nome.append(input("Digite o nome do aluno: "))
    nota[i] = float(input("Digite sua nota: "))
for i in range(3):#10
    if(i == 0):
        menor = nota[i]
        nomemenor = nome[i]
        notamenor = nota[i]
        maior = nota[i]
        nomemaior = nome[i]
        notamaior = nota[i]
    if(nota[i] < menor):
        nomemenor = nome[i]
        notamenor = nota[i]
        menor = nota[i]
    if(nota[i] > maior):
        nomemaior = nome[i]
        notamaior = nota[i]
        maior = nota[i]
print(f"{nomemenor} foi o aluno que recebeu a menor nota: {notamenor}")
print(f"{nomemaior} foi o aluno que recebeu a maior nota: {notamaior}")