qnt = 3 #10
pos = 0
matriz = [[0 for i in range(3)] for i in range(qnt)]
for i in range(qnt):
    for j in range(3):
        if(j == 0):
            matriz[i][j] = input()
        else:
            matriz[i][j] = int(input())
        if(i == 0):
            maior = matriz[i][2]
        if(matriz[i][2] > maior):
            maior = matriz[i][2]
            pos = i
cr = matriz[pos][0][3] + matriz[pos][0][4] + matriz[pos][0][5]
#cr = int(cr)
matricula = matriz[pos][0][6] + matriz[pos][0][7] + matriz[pos][0][8]
#matricula = int(cr)
print(f'A aluna com maior CR foi:\nMatrícula: {matricula}\nCoeficiente de rendimento: {maior}\nCódigo: {cr}')

#print(matriz[0][0][3])