/*Escreva um algoritmo que realize a potência de A (número real) por B (número inteiro e positivo)
, ou seja, AB, através de multiplicações sucessivas. Esses dois valores são passados pelo usuário através do teclado.*/
#include <stdio.h>
#include <stdlib.h>

int main(){
    int a, b, resultado = 1;

    printf("Digite um valor de para A e B: ");
    scanf("%d %d", &a, &b);

    for(int i = 0; i < b; i++){
        resultado = resultado * a;
    }

    printf("O resultado e: %d", resultado);
    return 0;
}