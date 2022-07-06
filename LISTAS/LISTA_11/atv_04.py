NomeArquivo = input('Arquivo 1: ')
NomeArquivo2 = input('Arquivo 2: ')
arquivo1 = open(NomeArquivo, 'r')
arquivo2 = open(NomeArquivo2, 'w')
for i in arquivo1:
    arquivo2.write(str(i))
arquivo1.close()
arquivo2.close()