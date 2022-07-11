/*Escreva um algoritmo que leia um número e escreva a raiz quadrada do número caso ele seja positivo ou igual a zero
e o quadrado do número caso ele seja negativo.*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int x, raiz;
    raiz = 0;

    printf("Digite um numero: ");
    scanf("%d", &x);

    if(x >= 0){
        raiz = sqrt(x);
        printf("%d \n", raiz);
    }
    
    return 0;
}