#include <stdio.h>
#include <stdlib.h>

void invertido(char x[3]);

int main(){
    char num[3];

    printf("Digite um numero: ");
    scanf("%s", &num);
    invertido(num);
    printf("Numero invertido: %s", num);
    return 0;
}

void invertido(char x[3]){
    int i;
    char aux;
        aux = x[0];
        x[0] = x[2];
        x[2] = aux;
}