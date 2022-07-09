'''
5. Faça um programa que recebe os nomes de dois arquivos. O primeiro arquivo contém nomes de alunos e o segundo arquivo 
contém as notas dos alunos. No primeiro arquivo, cada linha corresponde ao nome de um aluno e no segundo arquivo, cada 
linha corresponde às notas dos alunos (uma ou mais). Assuma que as notas foram armazenadas como strings, e estão separadas 
umas das outras por espaços em branco. Leia os dois arquivos e gere um terceiro arquivo que contém o nome do aluno seguido 
da média de suas notas.

#COMO EU ESTAVA FAZENDO!
#Arquivo de nomes
nome1 = input('Arquivo 1: ')
#Arquivo de notas
nome2 = input('Arquivo 2: ')
nome3 = input('Nome do Arquivo 3: ')
arquivo1 = open(nome1, 'r')
arquivo2 = open(nome2, 'r')
arquivo3 = open(nome3, 'w')
vetornomes = []
vetornotas = []
for i in arquivo1:
    vetornomes.append(i)
for i in arquivo2:
    vetornotas.append(i)

for i in range(len(vetornomes)):
    arquivo3.write(vetornomes[i])
    arquivo3.write(' ')
    arquivo3.write(vetornotas[i])
    arquivo3.write('\n')

arquivo1.close()
arquivo2.close()
arquivo3.close()

#Utilizei↓
#https://pt.stackoverflow.com/questions/485810/uma-fun%C3%A7%C3%A3o-que-recebe-como-argumentos-os-nomes-de-dois-arquivos

Arquivo Aluno↓
Sophia MARQUES
Maria Julia  MACHADO
Maria Cecilia LOPES
Maria Clara LIMA
Heloisa  GONCALVES

Arquivo notas↓
10 20
30 40
50 60
70 80
90 100

'''
lista = []
arqnome = input('Aruivo dos nome: ')
fAluno = open(arqnome, 'r')
alunos = fAluno.readlines()
fAluno.close()

arqnota = input('Arquivo das notas: ')
fNota = open(arqnota, 'r')
notas = fNota.readlines()
fNota.close()

for n in range(len(alunos)):
    aluno = alunos[n].replace('\n', '')
    nota = notas[n].replace('\n', '').split(' ')
    valor = [int(val) for val in nota]
    lista.append([aluno,valor])
    
arquivo = open('media.txt', 'w')
for n in range(len(lista)):
    aluno = lista[n][0]
    media = (lista[n][1][0] + lista[n][1][1])/2
    #media = sum(lista[n][1])/2
    arquivo.write(aluno +' '+str(media)+'\n')
arquivo.close()
