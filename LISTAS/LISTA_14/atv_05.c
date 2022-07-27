#include <stdio.h>
#include <stdlib.h>

int MDC(int x, int y);

int main(){
    int num1, num2;
    scanf("%d%d", &num1, &num2);
    if(num1 >= num2)
        printf("%d", MDC(num1, num2));
    else
        printf("%d", MDC(num2, num1));
    return 0;
}
int MDC(int x, int y){
    int a = x - y;
    if(a == y)
        return a;
    if(y > a)
        MDC(y, a);
    else
        MDC(a, y);
}