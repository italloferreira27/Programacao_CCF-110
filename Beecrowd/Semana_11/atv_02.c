#include <stdio.h>
#include <stdlib.h>
//#include <math.h>

int main(){

    double raio, area, expo;

    scanf("%lf", &raio);
    //expo = exp(raio);
    area = (raio * raio) * 3.14159;

    printf("A=%.4lf\n", area);
    return 0;
}