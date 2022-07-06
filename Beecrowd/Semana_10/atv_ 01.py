vetorpar = []
vetorimpar = []
contpar = 0
contimpar = 0
c = 0

for i in range(15):
    x = int(input())
    if(x % 2 == 0):
        vetorpar.append(x)
        contpar += 1
    else:
        vetorimpar.append(x)
        contpar += 1

for i in range(10):
    if(i < 5):
        print(f'par[{i}] = {vetorpar[i]}')
        vetorpar.remove(vetorpar[i])
    elif(i > 4 and i < 10):
        print(f'impar[{c}] = {vetorimpar[c]}')
        vetorimpar.remove(vetorimpar[i])
        c += 1
        
c, a = 0        
try:
    print(f'impar[{c}] = {vetorimpar[c]}')
    c += 1
except ValueError:
    print(f'par[{a}] = {vetorpar[a]}')
    a += 1
