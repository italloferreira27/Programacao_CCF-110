#include <stdio.h>
#include <stdlib.h>

void mult(float x1, float x2);
void divisao(float x1, float x2);
void som(float x1, float x2);
void sub(float x1, float x2);
void elv(float x1, float x2);

int main(){
    float x1, x2;
    char op;

    printf("Entre com dois numeros e a operacao que deseja |EX: (x1 * x2)|: ");
    scanf("%f %s %f", &x1, &op, &x2);

    switch(op){
    case '*':
    mult(x1, x2);
    break;
    case '/':
    divisao(x1, x2);
    break;
    case '+':
    som(x1, x2);
    break;
    case '-':
    sub(x1, x2);
    break;
    case '^':
    elv(x1, x2);
    break;
    }
    return 0;
}

void mult(float x1, float x2){
    int res = 0;
    for(int i = 0; i < x2; i++){
        res += x1;
    }
    printf("Resultado: %d", res);
}
void divisao(float x1, float x2){
    float res;
    res = x1 / x2;
    printf("Resultado: %.2f", res);
}
void som(float x1, float x2){
    int res = 0;
    res = x1 + x2;
    printf("Resultado: %d", res);
}
void sub(float x1, float x2){
    int res = 0;
    res = x1 - x2;
    printf("Resultado: %d", res);
}
void elv(float x1, float x2){
    int res = 1;
    for(int i = 0; i < x2; i++){
        res *= x1;
    }
    printf("Resultado: %d", res);
}