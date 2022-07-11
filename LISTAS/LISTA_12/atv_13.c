/*Crie um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva os elementos da diagonal principal.*/

#include <stdio.h>
#include <stdlib.h> //Biblioteca para gerar numeros aleatórios


int main(){
    int matriz[10][10];

    //Preenchendoa matriz com numeros aleatorios de 0 a 10
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            matriz[i][j] = ("%d", rand() % 10);
        }
    }

    //Escrevendo a matriz
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            printf("%d", matriz[i][j]);
            printf(" ");
        }
        printf("\n");
    }

    //Escrevendo os elementos
    printf("\nEscrevendo od elementos da diagonal principal:\n");
    for(int i = 0; i < 10; i++){
        printf("%d", matriz[i][i]);
        printf(" ");
     }

    return 0;
}