tamanhovetor = int(input("Digite eo tamanho do vetor: "))
vetor = [0 for i in range(tamanhovetor)]
contador = 0
print("Preencha o vetor: ")
for i in range(tamanhovetor):
    vetor[i] = int(input())
for i in range(tamanhovetor):
    if(vetor[i]%2==0):
        contador += vetor[i]
print(f"A soma dos índices pares é de: {contador}") 