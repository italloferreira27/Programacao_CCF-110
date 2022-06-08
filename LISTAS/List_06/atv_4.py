vt = [0 for i in range(5)]#25
true = []
for i in range(5):#25
    vt[i] = int(input())
num = int(input('Digite o valor n: '))
for i in range(5):#25
    if(num == vt[i]):
        #print(f"Esse número está na posição {i} do vetor.")
        true.append(i)
if(true):
    print(f"Esse número está na posição {true} do vetor.")
else:
    print("*ERRO esse número não está no vetor.*")

#...................OUTRA FORMA DE FAZER A 4...................

#vt = [0 for i in range(5)]#25
#true = 0
#for i in range(5):#25
#    vt[i] = int(input())
#num = int(input('Digite o valor n: '))
#for i in range(5):#25
#    if(num == vt[i]):
#        print(f"Esse número está na posição {i} do vetor.")
#        true += 1
#if(true==0):
#    print("*ERRO esse número não está no vetor.*")