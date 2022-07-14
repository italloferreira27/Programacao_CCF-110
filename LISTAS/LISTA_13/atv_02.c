#include <stdio.h>
#include <stdlib.h>

int PAR(int x);

int main(){
    int x, d;

    printf("Digite um numero: ");
    scanf("%d", &x);
    d = PAR(x);
    printf("%d", d);
    
    return 0;
}

int PAR(int x){
    if(x%2==0)
        return 0;
    return 1;
}