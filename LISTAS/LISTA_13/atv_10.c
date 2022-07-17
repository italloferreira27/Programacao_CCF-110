#include <stdio.h>
#include <stdlib.h>

void menor(float * n);

int main(){
    float num[3];

    printf("Digite tres numeros: ");
    for(int i = 0; i < 3; i++){
        scanf("%f", &num[i]);
    }
    menor(num);
    return 0;
}
void menor(float * n){
    float menor = n[0];
    for(int i = 0; i < 3; i++){
        if(menor > n[i])
            menor = n[i];
    }
    printf("%.2f", menor);
}