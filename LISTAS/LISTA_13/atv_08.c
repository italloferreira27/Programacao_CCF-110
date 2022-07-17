#include <stdio.h>
#include <stdlib.h>

float Conversor(float m);

int main(){
    float med;
    printf("Digite sua medida: ");
    scanf("%f", &med);
    Conversor(med);

    return 0;
}
float Conversor(float m){
    float pol, pe;
    pol = m * 39.37;
    pe = pol / 12;
    printf("%.2f metros equivale a %.2f polegadas.\n", m, pol);
    printf("%.2f metros equivale a %.2f pes.", m, pe);
    return 0;
}