#include <stdio.h>
#include <stdlib.h>

int main(){

    int a, b, c, d;

    scanf("%d %d %d %d", &a, &b, &c, &d);

    
    if(b > c && d > a && (c+d) > (a+b) && a % 2 == 0){
     printf("\nValores aceitos");
    }
    else
        printf("\nValores nao aceitos");
    return 0;
}