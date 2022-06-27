palavra1 = input('Digite a primeira palavra: ')
palavra2 = input('Digite a segunda palavra: ')
cont = 0
for i in range(len(palavra1)):
    if(palavra1[i] == palavra2[len(palavra1)-1-i]):
        cont += 1

if(cont == len(palavra1)):
    print('Essas palavras são palíndromas mútuas!')
else:
    print('Essas palavras NÃO são palíndromas mútuas!')