/*Escreva um algoritmo que leia um vetor de tamanho n (informado pelo usuário) 
e escreva a soma de todos os elementos de índice par.*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    int n;

    printf("Digite o tamnho do vetor: ");
    scanf("%d", &n);

    int vetor[n];

    printf("Preencha o vetor: \n");
    for(int i = 0; i < n; i++){
        scanf("%d", &vetor[i]);
    }

    printf("Valores do vetor com o indice par: ");
    for(int i = 0; i < n; i=i+2){
        printf("%d", vetor[i]);
        printf(" ");
    }
    return 0;
}