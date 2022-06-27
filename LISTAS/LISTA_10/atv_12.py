frase = input('Digite uma frase: ')
newfrase = []
for i in range(len(frase)):
    if(frase[i] != ' '):
        newfrase.append(frase[i])
    else:
        newfrase.append('#')

for i in range(len(frase)):
    print(newfrase[i], end="")