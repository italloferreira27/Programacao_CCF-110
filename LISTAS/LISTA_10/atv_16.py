nome = input('Digite seu nome: ')
vtm = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vtM = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
newnome = []
for i in range(len(nome)):
    for j in range(26):
        if(nome[i] == vtm[j] or nome[i] == vtM[j]):
            newnome.append(vtM[j])
            for i in range(len(newnome)):
                print(newnome[i], end="")
    print()