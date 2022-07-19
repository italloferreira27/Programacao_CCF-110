#include <stdio.h>
#include <stdlib.h>

int main() {
 
    int n, quad;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            quad = pow(i, 2);
            printf("%d^2 = %d\n", i, quad);
        }
    } 
    return 0;
}