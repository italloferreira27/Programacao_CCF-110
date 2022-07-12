/*Construa um algoritmo para fazer a soma de vários valores inteiros e positivos,
fornecidos pelo usuário através do teclado. O dado que finaliza a sequência de entrada é o número –1,
e este não deve ser considerado.*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    
    int n, soma = 0;
    
    while(1){
        printf("Digite um numero: ");
        scanf("%d", &n);

        if(n != -1){
            if(n >= 0){
                soma = soma + n;
                n = 0;
            }
        }

        else
            break;
    }
    printf("A soma dos numeros e: %d", soma);
    return 0;
}