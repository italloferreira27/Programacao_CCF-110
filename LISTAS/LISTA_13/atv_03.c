#include <stdio.h>
#include <stdlib.h>

int primo(int x);

int main(){
    int x, aux;

    printf("Digite um numero: ");
    scanf("%d", &x);

    aux = primo(x);
    printf("%d", aux);
    
    return 0;
}

int primo(int x){
    int i, cont = 0;

    for(i = 1; i <= x; i++){
        if(x % i == 0)
            cont++;
    }
    if(cont == 2)
        return 1;
    return 0;
}