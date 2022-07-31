#include <stdio.h>
#include <stdlib.h>

void impares(int ini, int fim);

int main(){
    int i,f;
    scanf("%d%d", &i, &f);
    if(i % 2 == 0)
        i = i + 1;
    printf("%d ", i);
    impares(i, f);
    return 0;
}
void impares(int ini, int fim){
    if(ini < fim-2){
        ini = ini + 2;
        printf("%d ", ini);
        impares(ini, fim);
    }
}