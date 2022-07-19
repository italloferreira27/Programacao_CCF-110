#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float Delta(float a, float b, float c);
void Raiz(float b, float del, float a);

int main(){
    float a, b, c, d = 0;

    printf("|ax2 + bx + c|\nDigite os termos a b e c: ");
    scanf("%f %f %f", &a, &b, &c);
    
    d = Delta(a, b, c);
    printf("Delta: %.2f\n", d);
    Raiz(b, d, a);
    
    return 0;
}

float Delta(float a, float b, float c){
    float del;
    del = ((b*b) - (4*a*c));
    return del;
}

void Raiz(float b, float del, float a){
    float raiz1, raiz2;
    if(del < 0){
        printf("Nao existe raiz real!");
    }
    if(del == 0){
        raiz1 = -b / 2*a;
        printf("Existe uma raiz: %f", raiz1);
    }
    if(del > 0){
        raiz1 = (-b + sqrt(del))/2*a;
        raiz2 = (-b - sqrt(del))/2*a;
        printf("\nExiste duas raizes:\nRaiz 1 = %.2f", raiz1);
        printf("\nRaiz 2 = %.2f", raiz2);
    }
    
}