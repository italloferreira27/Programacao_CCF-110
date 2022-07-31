#include <stdio.h>
#include <stdlib.h>

int resto(int x, int y){
    if(y == 0)
        return -1;
    if(x >= y)
        return resto((x-y), y);
    else
        return x;
}

int main(){
    int num1, num2, valor;
    printf("Digite dois numeros: ");
    scanf("%d %d", &num1, &num2);
    if(num1 < 0)       
        num1 = num1 * -1;
    if(num2 < 0)       
        num2 = num2 * -1;

    valor = resto(num1, num2);
    printf("%d mod %d = %d", num1, num2, valor);

    printf("\n%d", (num1 % num2));
    return 0;
}