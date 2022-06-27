i = 0
matriz = [[0 for j in range(2)] for i in range(1)]
while i < 300:
    aluno = int(input('Digite sua matricula: '))
    confirm = input('Vc vai guardar lugar - |SIM| ou |NAO|: ')

    if(confirm == 'SIM'):
        lugares = int(input('Quantos lugares: '))
        refeitorio = input('Vcs vão comer no refeitório - |SIM| NAO:')
        if(refeitorio == 'SIM'):
            matriz.append([aluno, lugares+1])
            i += lugares+1

    else:
        refeitorio = input('Você vai comer no refeitório - |SIM| |NAO|:')
        if(refeitorio == 'SIM'):
            matriz.append([aluno, 1])
            i += 1
    print()

print('O refeitório encheu: ')
for i in range(len(matriz[i])):
        print(f'O aluno {matriz[i][0]} vai comer no refeitório com {matriz[i][1]} pessoas.')