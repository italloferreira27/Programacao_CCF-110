/*Considerando a série abaixo, escreva um algoritmo que seja capaz de gerar seus N termos.
 Esse número N deve ser lido do teclado.*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    int n;

    printf("Digite o valor de n: ");
    scanf("%d", &n);

    if(n > 0){
        printf("S = ");
        for(int i = 1; i <= n; i++){
            printf("%d", i);
            printf(",");
            printf("%d", 3+i);
            printf(",");
            printf("%d", 3+i);
            printf(",");
        }
    }
    return 0;
}