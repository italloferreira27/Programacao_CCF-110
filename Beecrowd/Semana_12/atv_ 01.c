#include <stdio.h>
#include <stdlib.h>

int main(){
    int valor, x, x100 = 0, x50 = 0, x20 = 0, x10 = 0, x5 = 0, x2 = 0, x1 = 0;

    scanf("%d", &valor);

    x100 = valor / 100;
    x = valor % 100;
    // printf("valor x: %d\n", x);
    // printf("%d \n%d", x100, x);
    if(x >= 50){
        x50 = x / 50;
        x = x % 50;

    }
    // printf("valor x: %d\n", x);
    if(x >= 20){
        x20 = x / 20;
        x = x % 20;
    }
    // printf("valor x: %d\n", x);
    if(x >= 10){
        x10 = x / 10;
        x = x % 10;
        // printf("Valor de 10: %d   valor de x: %d\n", x10, x);
    }
    // printf("valor x: %d\n", x);
    if(x >= 5){
        x5 = x / 5;
        x = x % 5;
    }
    // printf("valor x: %d\n", x);
    if(x >= 2){
        x2 = x / 2;
        x = x % 2;
    }
    x1 = x;
        printf("%d\n", valor);
        printf("%d nota(s) de R$ 100,00\n", x100);
        printf("%d nota(s) de R$ 50,00\n", x50);
        printf("%d nota(s) de R$ 20,00\n", x20);
        printf("%d nota(s) de R$ 10,00\n", x10);
        printf("%d nota(s) de R$ 5,00\n", x5);
        printf("%d nota(s) de R$ 2,00\n", x2);
        printf("%d nota(s) de R$ 1,00\n", x1);
    return 0;
}