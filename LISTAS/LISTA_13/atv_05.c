#include <stdio.h>
#include <stdlib.h>

void fah_cel(float x);
void fah_kel(float x);
void cel_fah(float x);
void cel_kel(float x);
void kel_fah(float x);
void kel_cel(float x);


int main(){
    int tmp, conv;
    float temp, celsius, fahrenheit, kelvin;
    printf("Digite sua temperatura: ");
    scanf("%f", &temp);
    printf("\n0 - Fahrenheit para Celsius;\n1 - Fahrenheit para Kelvin;\n2 - Celsius para Fahrenheit;\n3 - Celsius para Kelvin;\n4 - Kelvin para Fahrenheit;\n5 - Kelvin para Celsius.\nDIGITE A MANEIRA DE CONVERSAO:");
    scanf("%d", &conv);
    switch(conv){
        case 0:
            fah_cel(temp);
        break;
        case 1:
            fah_kel(temp);
        break;
        case 2:
            cel_fah(temp);
        break;
        case 3:
            cel_kel(temp);
        break;
        case 4:
            kel_fah(temp);
        break;
        case 5:
            kel_cel(temp);
        break;

    }
    return 0;
}
//Tem como fazer um switch case com 2 variaveis?

void fah_cel(float x){
    float cel;
    cel = (x-32)/1.8;
    printf("Temperatura em Celsius: %.2f", cel);
}
void fah_kel(float x){
    float kel;
    kel = (((x - 32) * 5) / 9) + 273.15;
    printf("Temperatura em Kelvin: %.3f", kel);
}
void cel_fah(float x){
    float fah;
    fah = ((x*9)/5 + 32);
    printf("Temperatura em Fahrenheit: %.2f", fah);
}
void cel_kel(float x){
    float kel;
    kel = x + 273.15;
    printf("Temperatura em Kelvin: %.2f", kel);
}
void kel_fah(float x){
    float fah;
    fah = (((x-273.15)*9)/5 + 32);
    printf("Temperatura em Fahrenheit: %.2f", fah);
}
void kel_cel(float x){
    float cel;
    cel = x-273.15;
    printf("Temperatura em Celsius: %.2f", cel);
}