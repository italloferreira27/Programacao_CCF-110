#include <stdio.h>
#include <stdlib.h>

void troco(float x, float d);

int main(){
    float valor, dinc;
    printf("Valor da compra (em centavos): ");
    scanf("%f", &valor);
    printf("Valor recebido (em centavos): ");
    scanf("%f", &dinc);
    troco(valor, dinc);
    return 0;
}
void troco(float x, float d){
    int r;
    float qnt;
    if(d < x)
        printf("O VALOR E INSUFICIENTE!");
    if(x == d)
        printf("NAO HA TROCO!");
    if(d > x){
        r = d - x;
        if(r >= 50){
            qnt = (r / 50);
            r = (r % 50);
            printf("%.0f moedas de 50 centavos.\n", qnt);
        }
        if(r >= 20){
            qnt = (r / 20);
            r = (r % 20);
            printf("%.0f moedas de 20 centavos.\n", qnt);
        }
        if(r >= 10){
            qnt = (r / 10);
            r = (r % 10);
            printf("%.0f moedas de 10 centavos.\n", qnt);
        }
        if(r  >= 5){
            qnt = (r / 5);
            r = (r % 5);
            printf("%.0f moedas de 5 centavos.\n", qnt);
        }
        if(r >= 2){
            qnt = (r / 2);
            r = (r % 2);
            printf("%.0f moedas de 2 centavos.\n", qnt);
        }
        if(r >= 1)
            printf("%d moedas de 1 centavo.\n", r);
    }
}