#include <stdio.h>
#include <stdlib.h>

void triangulo(int a, int b, int c);

int main(){
    int l1, l2, l3;
    printf("Digite os tres lados de um triangulo: ");
    scanf("%d %d %d", &l1, &l2, &l3);
    triangulo(l1, l2, l3);
    return 0;
}
void triangulo(int a, int b, int c){
    if(a > (b - c) && a < (b + c) && b > (a - c) && b < (a + c) && c > (b - a) && c < (b + a)){
        if(a == b && b == c)
            printf("Triangulo EQUILATERO!");
        if(a == b && b != c || a == c && b != c || b == c && a != c)
            printf("Triangulo ISOSCELES!");
        if(a != b && b != c)
            printf("Triangulo ESCALENO!");
    }
    else
        printf("NAO E UM TRIANGULO!");
}