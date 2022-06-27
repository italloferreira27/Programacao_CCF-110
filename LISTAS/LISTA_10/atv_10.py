dna = input('Digite a cadeia de DNA: ')
rna = []
for i in range(len(dna)):
    if(dna[i] == 'A'):
        rna.append('T')

    elif(dna[i] == 'T'):
        rna.append('A')

    elif(dna[i] == 'C'):
        rna.append('G')

    elif(dna[i] == 'G'):
        rna.append('C')

for i in range(len(dna)):      
    print(rna[i], end="")