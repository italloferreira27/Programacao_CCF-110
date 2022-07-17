#include <stdio.h>
#include <stdlib.h>

void Pos_Neg(int x);

int main(){
    int num;
    printf("Digite um numero inteiro: ");
    scanf("%d", &num);
    Pos_Neg(num);
    return 0;
}
void Pos_Neg(int x){
    if(x > 0)
        printf("Numero POSITIVO!");
    if(x == 0)
        printf("Numero NULO!");
    else
        printf("Numero NEGATIVO!");
}