import random
qntnomes = int(input("Quantos nomes você quer adicionar: "))
nomearquivo = input("Arquivo: ")
arquivo = open(nomearquivo, 'w')
ListaNomes = ['Sophia', 'Maria Julia ', 'Maria Cecilia', 'Maria Clara', 'Heloisa ', 'Joao Miguel', 'Samuel ', 'Bernardo ', 'Gabriel ', 'Davi ', 'Valentina ', 'Maria Alice', 'Laura ', 'Alice ', 'Helena ', 'Theo', 'Heitor', 'Gael', 'Arthur', 'Miguel']
listaSobrenomes = ['MARQUES', 'MACHADO', 'LOPES', 'LIMA', 'GONCALVES', 'GOMES', 'GARCIA', 'FERREIRA', 'FERNANDES', 'FREITAS', 'DUARTE', 'DIAS', 'COSTA', 'CASTRO', 'CARVALHO', 'CARDOSO', 'CAMPOS', 'SILVA', 'OLIVEIRA', 'ALVES']

for i in range(qntnomes):
    arquivo.write(ListaNomes[i])
    arquivo.write(' ')
    arquivo.write(listaSobrenomes[i])
    arquivo.write(', ')
    arquivo.write(str(random.randrange(0, 100)))
    arquivo.write(' Anos,')
    arquivo.write(' ')
    arquivo.write(str(round(random.uniform(1.50, 2.30), 2)))
    arquivo.write(' de altura.')
    arquivo.write('\n')
print("Nomes adicionados com sucesso!")
arquivo.close()