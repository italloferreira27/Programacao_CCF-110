#import os
#print(os.getcwd)

print('Adicionar de 200 a 50 em um arquivo.')
nomearquivo = input('Arquivo: ')
arquivo = open(nomearquivo, 'w')
for i in range(200, 49, -1):
    arquivo.write(str(i))
    arquivo.write('\n')
print('Números adicionados com sucesso!')
arquivo.close()