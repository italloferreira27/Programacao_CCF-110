#include <stdio.h>
#include <stdlib.h>

int Quociente(int x, int y){
    if(y == 0)
        return -1;
    if(x == 0 || x < y)
        return 0;
    if(x == y){
        return 1;
    }
    return 1 + Quociente((x - y), y);
}

int main(){
    int num1, num2, valor;
    printf("Digite dois numeros: ");
    scanf("%d %d", &num1, &num2);
    if(num1 >= 0 && num2 >= 0)
        valor = Quociente(num1, num2);
    if(num1 < 0 && num2 < 0)
        valor = Quociente((num1 * -1), (num2 * -1));
    if(num1 < 0 && num2 > 0)
        valor = -Quociente((num1 * -1), (num2));
    if(num1 > 0 && num2 < 0)
        valor = -Quociente((num1), (num2 * -1));

    printf("%d / %d = %d", num1, num2, valor);
    return 0;
}