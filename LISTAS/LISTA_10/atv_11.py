palavra = input()
cont = 0

if(palavra[0] != ' '):
    for i in range(len(palavra)-1):
        if(palavra[i] == ' ' and palavra[i+1] != ' '):
            cont += 1
    print('A frase tem ', cont+1, 'palavras.')

elif(palavra[0] == ' '):
    for i in range(len(palavra)-1):
        if(palavra[i] == ' ' and palavra[i+1] != ' '):
            cont += 1
    print('A frase tem ', cont, 'palavras.')

