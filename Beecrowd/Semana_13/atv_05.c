#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int n, compradas, prom, div;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d %d", &compradas, &prom);
        if(compradas >= prom){
            div = compradas / prom;
            div += compradas % prom;
            printf("%d\n", div);
        }
        else
            printf("%d\n", compradas);
    }
    return 0;
}