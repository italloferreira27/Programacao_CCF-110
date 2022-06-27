tm = 1
#achei = 0
valor = True
matriz = [[0 for j in range(2)] for i in range(tm)]

while True:
    if(valor):
        for i in range(tm):
            for j in range(2):
                matriz[i][j] = input()
                
    else:
        nome = input('Nome: ')
        num = input('Número: ')
        matriz.append([nome, num])
        tm += 1
     
    for i in range(tm):
        for j in range(i+1, tm):
            if(matriz[i][0] > matriz[j][0]):
                #nome = matriz[i][0]
                #matriz[i][0] = matriz[j][0]
                #matriz[i][0] = nome
                matriz[i][0], matriz[j][0] = matriz[j][0], matriz[i][0]
                #numero = matriz[i][1]
                #matriz[i][1] = matriz[j][1]
                #matriz[j][1] = numero
                matriz[i][1], matriz[j][1] = matriz[j][1], matriz[i][1]
    
    print('\nLISTA:')
    for i in range(tm):
        for j in range(2):
            print(matriz[i][j], end=" ")
        print()
    print()
    
    print('NOVO - PARA ADICIONAR UM NOVO NÚMERO:\nPROCURAR - PARA PROCURAAR UM NÚMERO DE TELEFONE:')
    confirm = input('→')

    if(confirm == 'NOVO'):
        valor = False
        continue
    
    elif(confirm == 'PROCURAR'):
        procurar = input('Digite o nome: ')
        for i in range(tm):
            if(procurar == matriz[i][0]):
                achei = matriz[i][0]
                numero = matriz[i][1]
        if(achei != 0):
            print(achei, numero)
        else:
            print('Número não listado!')
        break
    
    else:
        break