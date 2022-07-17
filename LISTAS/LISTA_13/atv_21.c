#include <stdio.h>
#include <stdlib.h>

float Soma_quadrado(float * vetor);

int main(){
    float num[20], res;
    printf("Preencha o vetor: ");
    for(int i = 0; i < 20; i++){
        scanf("%f", &num[i]);
    }
    res = Soma_quadrado(num);
    printf("A soma dos quadrados dos vetorres e %.2f", res);
    return 0;
}
float Soma_quadrado(float * vetor){
    float soma;
    for(int i = 0; i < 20; i++){
        soma += pow(vetor[i], 2);
    }
    return soma;
}