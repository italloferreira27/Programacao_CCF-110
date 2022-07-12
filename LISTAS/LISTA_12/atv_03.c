/*Dados três valores A, B e C, construa um algoritmo que escreva os valores de forma descendente
(do maior para o menor).*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, vetor[3], troca;

    for(i = 0; i < 3; i++){
        printf("Digite o valor: ");
        scanf("%d", &vetor[i]);
    }

    for(int i = 0; i < 3; i++){
        for(int j = i; j < 3; j++){
            if(vetor[i] < vetor[j]){
                troca = vetor[i];
                vetor[i] = vetor[j];
                vetor[j] = troca;
            }
        }
    }

    printf("Valores ordenados:\n");
    for(int i = 0; i < 3; i++){
        printf("%d", vetor[i]);
        printf(" ");
    }
    
    return 0;
}

