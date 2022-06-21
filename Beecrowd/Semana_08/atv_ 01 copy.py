vetorpar = []
vetorimpar = []
contpar = 0
contimpar = 0

for i in range(15):
    x = int(input())
    if(x % 2 == 0):
        vetorpar.append(x)
        contpar += 1
        if(contpar == 5):
            for i in range(5):
                print(f'par[{i}] = {vetorpar[i]}')
            contpar = 0
            vetorpar = []

    else:
        vetorimpar.append(x)
        contimpar += 1
        if(contimpar == 5):
            for i in range(5):
                print(f'impar[{i}] = {vetorimpar[i]}')
            contimpar = 0
            vetorimpar = []
            
for i in range(contimpar):
    print(f'impar[{i}] = {vetorimpar[i]}')
for i in range(contpar):
    print(f'par[{i}] = {vetorpar[i]}')