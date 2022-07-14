#Trabalho Prático de Matemática Discreta

def OR(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if(x[i] or y[i] == 1):
            vetor[i] = '1'
        else:
            vetor[i] = '0'
    for i in range(n-1):
        print(vetor[i], end="") 
    return vetor[n-1]

def AND(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if(x[i] and y[i] == 1):
            vetor[i] = '1'
        else:
            vetor[i] = '0'
    for i in range(n-1):
        print(vetor[i], end="") 
    return vetor[n-1]

def XOR(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if((x[i] and not y[i]) or (not x[i] and y[i])):
            vetor[i] = '1'
        else:
            vetor[i] = '0'
    for i in range(n-1):
        print(vetor[i], end="") 
    return vetor[n-1]

def NAND(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if(x[i] == 1 and y[i] == 1):
            vetor[i] = '0'
        else:
            vetor[i] = '1'
    for i in range(n-1):
        print(vetor[i], end="") 
    return vetor[n-1]

def NOR(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if(x[i] == 0 and y[i] == 0):
            vetor[i] = '1'
        else:
            vetor[i] = '0'
    for i in range(n-1):
        print(vetor[i], end="") 
    return vetor[n-1]

def MOR(x, y, n):
    vetor = [0 for i in range(n)]
    for i in range(n):
        if((not x[i]) or y[i]):
            vetor[i] = '1'
        else:
            vetor[i] = '0'
    for i in range(n-1):
        print(vetor[i], end="") 
    return vetor[n-1]

#Entrada dos valores
n = int(input())
s1 = input()
S1 = list(map(int, s1))
s2 = input()
S2 = list(map(int, s2))
esp = input().split()

#Identificando S1 e S2
if(esp[0] == 'S1'):
    esp[0] = S1
if(esp[0] == 'S2'):
    esp[0] = S2
if(esp[2] == 'S1'):
    esp[2] = S1
if(esp[2] == 'S2'):
    esp[2] = S2

if(len(esp) == 5):
    if(esp[4] == 'S1'):
        esp[4] = S1
    if(esp[4] == 'S2'):
        esp[4] = S2

#Verificando se as informações são validas 
if(len(s1) == n and len(s2) == n):
    for i in range(n):
        if(s1[i] != 0 or s1[i] != 1 and s2[i] != 0 or s2[i] != 1 ):
            valor = True
        else:
            print("ERRO")
            break

    if(valor and len(esp) == 3):
        if(esp[1] == 'OR'):
            print(OR(esp[0], esp[2], n))
        if(esp[1] == 'AND'):
            print(AND(esp[0], esp[2], n))
        if(esp[1] == 'XOR'):
            print(XOR(esp[0], esp[2], n))
        if(esp[1] == 'NAND'):
            print(NAND(esp[0], esp[2], n))
        if(esp[1] == 'NOR'):
            print(NOR(esp[0], esp[2], n))
        if(esp[1] == 'MOR'):
            print(MOR(esp[0], esp[2], n))
        print("ERRO")

else:
    print("ERRO")