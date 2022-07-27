#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int i, j, n, troca, valor = 0;
    scanf("%d", &n);
    int num[n];
    for(i = 1; i < n; i++){
        scanf("%d", &num[i]);
        }
    for(i = 1; i < n; i++){
        for(j = i+1; j < n; j++){
            if(num[i] > num[j]){
                troca = num[i];
                num[i] = num[j];
                num[j] = troca;
            }
        }
    }
    for(i = 1; i <= n; i++){
        if(num[i] != i){
            valor = i;
            break;
        }
    }
    printf("%d\n", valor);
    return 0;
}