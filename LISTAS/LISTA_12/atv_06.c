#include <stdio.h>
#include <stdlib.h>

int main(){
    int s, soma = 0;

    for(int i = 1; i < 38; i++){
        s = ((38-i) * (39-i))/i;
        soma = soma + s;
    }

    printf("A soma e = %d", soma);
return 0;
}