/*Elabore um algoritmo que crie dois vetores com 10 posições. O usuário digitará os valores do primeiro vetor. 
O segundo vetor vai receber os valores do primeiro vetor em ordem invertida (o último elemento do primeiro 
vetor será o primeiro do segundo, o penúltimo elemento do primeiro vetor será o segundo elemento e assim por diante).*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int vt1[10], vt2[10];

    printf("Preencha o vetor 1:\n");
    for(int i = 0; i < 10; i++){
        scanf("%d", &vt1[i]);
    }

    //Substituindo os valores↓
    for(int i = 9; i > -1; i--){
        vt2[9-i] = vt1[i];
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