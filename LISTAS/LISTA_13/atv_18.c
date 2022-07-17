#include <stdio.h>
#include <stdlib.h>

void crescente(int * vet);

int main(){
    int vetor[10];
    printf("Preencha o vetor: ");
    for(int i = 0; i < 10; i++){
        scanf("%d", &vetor[i]);
    }
    crescente(vetor);
}
void crescente(int * vet){
    int troca;
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            if(vet[i] < vet[j]){
                troca = vet[i];
                vet[i] = vet[j];
                vet[j] = troca;
            }
        }
    }
    printf("Vetor ordenado: ");
    for(int i = 0; i < 10; i++){
        printf("%d", vet[i]);
        printf(" ");
    }
    return 0;
}