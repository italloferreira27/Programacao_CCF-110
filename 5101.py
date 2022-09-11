#Trabalho prático de M.D.
def OR(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if(x[i] == 1 or y[i] == 1):
            vetor[i] = '1'
        else:
            vetor[i] = '0' 
    return vetor

def AND(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if(x[i] and y[i] == 1):
            vetor[i] = '1'
        else:
            vetor[i] = '0'
    return vetor

def XOR(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if((x[i] and not y[i]) or (not x[i] and y[i])):
            vetor[i] = '1'
        else:
            vetor[i] = '0'
    return vetor

def NAND(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if(x[i] == 1 and y[i] == 1):
            vetor[i] = '0'
        else:
            vetor[i] = '1'
    return vetor

def NOR(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if(x[i] == 0 and y[i] == 0):
            vetor[i] = '1'
        else:
            vetor[i] = '0'
    return vetor

def MOR(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if(x[i] == 1 and y[i] == 0):
            vetor[i] = '0'
        else:
            vetor[i] = '1'
    return vetor

n = int(input())
s1 = input().strip()
s2 = input().strip()
esp = input().split()
a = 0
val = []
cont = 0 #Serve para indentificar a varialvel "val" quando for 2 operadores
if(len(s1) == n and len(s2) == n and n <= 1000):
    for i in range(n):
        if(s1[i] == '1' or s1[i] == '0' and s2[i] == '1' or s2[i] == '0'):
            S1 = list(map(int, s1))
            S2 = list(map(int, s2))
        else:
            print("ERRO")
            exit()  
else:
    print("ERRO")
    exit()       

#Identificando S1 e S2 e atribuindo a variavel val
for i in esp:
    if(i == 'S1'):
        val.append(S1)
    elif(i == 'S2'):
        val.append(S2)  

for j in range(n):
    if(val[0][j] == 0 or val[0][j] == 1 and val[1][j] == 0 or val[1][j] == 1):
        valor = True
    else:
        valor = False
        break

if(valor):
    for i in range(1, (len(esp) - 1), 2):
        if(esp[i] == 'OR'):
            a = OR(val[cont], val[cont + 1], n)

        if(esp[i] == 'AND'):
            a = AND(val[cont], val[cont + 1], n)

        if(esp[i] == 'XOR'):
            a = XOR(val[cont], val[cont + 1], n)

        if(esp[i] == 'NAND'):
            a = NAND(val[cont], val[cont + 1], n)

        if(esp[i] == 'NOR'):
            a = NOR(val[cont], val[cont + 1], n)

        if(esp[i] == 'MOR'):
            a = MOR(val[cont], val[cont + 1], n)
        cont += 1
        val[1] = list(map(int, a))

    if(a != 0):
        for i in range(n):
            print(a[i], end="")
    else:
        print("ERRO")
else:
    print("ERRO")