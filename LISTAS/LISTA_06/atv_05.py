alunos = []
contador = 0
for i in range(3):#15
    alunos.append(float(input()))
    #alunos.append(map(float, input().split(" "))) #CONTADOR NAO FUNCIONA COM MAP
    contador += alunos[i]
media = contador/3#15 
print(f"A média das notas são: {media:.2f}")