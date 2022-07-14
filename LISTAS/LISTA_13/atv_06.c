#include <stdio.h>
#include <stdlib.h>

void media(float a, float b, float c); 

int main(){
    float n1, n2, n3, a;

    printf("Digite suas 3 notas: ");
    scanf("%f %f %f", &n1, &n2, &n3);

    media(n1, n2, n3);
    
    return 0;
}

void media(float a, float b, float c){
    float media;
    media = (a+b+c)/3;
    printf("Media das notas: %.2f", media);
    return media;
}