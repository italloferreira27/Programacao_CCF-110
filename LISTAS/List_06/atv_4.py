vt = [0 for i in range(5)]#25
for i in range(5):#25
    vt[i] = int(input())
num = int(input('Digite o valor n: '))
for i in range(5):#25
    if(num == vt[i]):
        print(f"Esse número está na posição {i} do vetor.")
    else:
        print("*ERRO esse número não está no vetor.*")
        #ESSE PRINT ESTÁ ERRADO