/*Leia valores inteiros para a matriz A[3x5]. Gere e escreva o vetor SL (soma das 3 linhas), onde cada elemento
é a soma dos elementos de uma linha da matriz A. Faça o trecho que gera a matriz SL separado (laços de repetição)
da entrada e da saída de dados.*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    int A[3][5], soma = 0, vetor[3];

    //Preenchendo as matrizA
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 5; j++){
            A[i][j] = ("%d", rand() % 10);
        }
    }
    //Escrevendo a matriz
    printf("MATRIZ A:\n");
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 5; j++){
            printf("%d", A[i][j]);
            printf(" ");
        }
        printf("\n");
    }
    //Somando os valores no vetor
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 5; j++){
            soma = soma + A[i][j];
        }
        vetor[i] = soma;
        soma = 0;
    }
    printf("Vetor = ");
    for(int i = 0; i < 3; i++){
        printf("%d", vetor[i]);
        printf(" ");
    }
    return 0;
}