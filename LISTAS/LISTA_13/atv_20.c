#include <stdio.h>
#include <stdlib.h>

void div_3(int * n);

int main(){
    int num[5];

    printf("Digite os cinco numeros: ");
    for(int i = 0; i < 5; i++){
        scanf("%d", &num[i]);
    }

    div_3(num);

    return 0;
}
void div_3(int * n){
    for(int i = 0; i < 5; i++){
        if(n[i] % 3 != 0)
            n[i] = 0;
    }
    printf("Sao divisiveis por 3 os seginte numeros:\n");
    for(int i = 0; i < 5; i++){
        if(n[i] != 0)
            printf("%d ", n[i]);
    }
}
//Como adicionar valor em vetor em c?