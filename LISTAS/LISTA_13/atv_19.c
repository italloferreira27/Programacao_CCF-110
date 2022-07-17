#include <stdio.h>
#include <stdlib.h>

void soma(int vet[15]);

int main(){
    int vetor[15];
    printf("Preencha o vetor: ");
    for(int i = 0; i < 15; i++){
        scanf("%d", &vetor[i]);
    }
    soma(vetor);
    return 0;
}
void soma(int vet[15]){
    int res = 0;
    for(int i = 0; i < 15; i++){
        res += vet[i];
    }
    printf("A soma e de %d", res);
}