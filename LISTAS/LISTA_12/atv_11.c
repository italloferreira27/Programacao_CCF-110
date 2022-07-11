/*Escreva um algoritmo que leia um vetor inteiro de 10 posições e crie um segundo vetor, 
substituindo os valores menores que 10 por 1.  Mostre os 2 vetores no final do algoritmo.*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    int vt1[10], vt2[10];
    
    printf("Preencha o vetor:\n");
    for(int i = 0; i < 10; i++){
        scanf("%d", &vt1[i]);
    }

    //Alocando os valores do vetor1 no vetor2 
    for(int i = 0; i < 10; i++){
        vt2[i] = vt1[i];
    }
    //Comparando e substituindo os valores
    for(int i = 0; i < 10; i++){
        if(vt1[i] < 10){
            vt2[i] = 10;
        }
    }

    printf("\nVetor 1:");
    for(int i = 0; i < 10; i++){
        printf("%d " "", vt1[i]);
    }
    printf("\nVetor 2:");
    for(int i = 0; i < 10; i++){
        printf("%d " "", vt2[i]);
    }
    return 0;
}