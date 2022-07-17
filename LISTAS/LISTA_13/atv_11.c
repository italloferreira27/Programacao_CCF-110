#include <stdio.h>
#include <stdlib.h>

float Area(float a, float b, float c);

int main(){
    float l1, l2, l3, area;
    printf("Digite od lados de um triangulo: ");
    scanf("%f %f %f", &l1, &l2, &l3);
    area = Area(l1, l2, l3);
    printf("A area do triangulo e de: %.2f", area);

    return 0;
}
float Area(float a, float b, float c){
    float p, A;
    p = (a + b + c)/2;
    A = sqrt((p*(p-a) * (p-b) * (p-c)));
    return A;
}