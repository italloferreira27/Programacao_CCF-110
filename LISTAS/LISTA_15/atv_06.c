#include <stdio.h>
#include <stdlib.h>

int fatorial(int n);

int main(){
    int num1;
    scanf("%d", &num1);
    printf("%d", fatorial(num1));
    return 0;
}
int fatorial(int n){
    if(n > 1){
        n = n * (fatorial(n-1));
    }
    else
        return n = 1;
 }