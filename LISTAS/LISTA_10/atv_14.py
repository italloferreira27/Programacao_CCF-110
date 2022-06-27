name = input('Digite seu nome: ')
newname = []
vtm = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vtM = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(len(name)-1, -1, -1):
    for j in range(26):
        if(name[i] == vtm[j]):
            newname.append(vtM[j])

for i in range(len(name)):
    print(newname[i], end="")