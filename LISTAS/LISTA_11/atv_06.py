'''
6. Faça um programa para alterar uma das notas de um aluno (usando os arquivos do exercício anterior). 
O programa deve receber o nome do aluno, a nota velha e a nova nota. 

ARQUIVOS↓
aluno.txt
Sophia MARQUES
Maria Julia MACHADO
Maria Cecilia LOPES
Maria Clara LIMA
Heloisa GONCALVES
Itallo Winicios

nota.txt
10 20
30 40
50 61
70 60
90 99
100 99

'''
pos = 0
cont = 0
lista = []
aluno = []

arqnome = input('Arquivo dos nomes: ')
Nome = open(arqnome, 'r')
nomes = Nome.readlines()
Nome.close()

arqnota = input('Arquivo das notas: ')
Nota = open(arqnota, 'r')
notas = Nota.readlines()
Nota.close()

#separando os nome e as notas e alocando em uma lista | transformando notas em inteiros 
for i in range(len(notas)):
    aluno.append(nomes[i].replace('\n', ''))
    nota = notas[i].replace('\n', '').split(' ')
    valor = [int(j) for j in nota]
    lista.append(valor)


nome_aluno = input('Digite o nome do aluno: ')
#Verificando se há aluno com esse nome no arquivo
for n in aluno:
    if(nome_aluno == n):
        pos = cont
    cont += 1

if(pos != 0):
    nota_velha = int(input('Digite a nota velha: '))
    nota_nova = int(input('Digite a nota nova: '))

#substituindo as notas antigas pela nova
    cont = 0
    for i in range(2):
        if(lista[pos][i] == nota_velha):
            lista[pos][i] = nota_nova
            cont += 1

#Colocando a nova nota no arquivo
    if(cont != 0):
        arqnota = open(arqnota, 'w')
        for i in range(len(notas)):
            arqnota.write(str(lista[i][0])+' '+str(lista[i][1])+'\n')
        arqnota.close()

    else:
        print('Nota não encontrada!')

else:
    print('Nome não encontrado!')