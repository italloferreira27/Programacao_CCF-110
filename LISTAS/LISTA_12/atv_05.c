/*Escreva um algoritmo que escreva todos os números múltiplos de 5, no intervalo fechado de 1 a 500.*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    for(int i = 1; i < 501; i++){
        if(i % 5 == 0){
            printf("%d", i);
            printf(" ");
        }
    }
    return 0;
}